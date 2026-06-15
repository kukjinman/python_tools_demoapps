param(
    [switch]$SkipInstall
)

$ErrorActionPreference = 'Stop'

if ([Environment]::OSVersion.Platform -ne [PlatformID]::Win32NT) {
    throw 'Windows EXE는 Windows 환경에서 빌드해야 합니다.'
}

$Root = $PSScriptRoot
$Venv = Join-Path $Root '.venv-windows-build'
$Python = Join-Path $Venv 'Scripts\python.exe'
$Work = Join-Path $Root 'build\pyinstaller'
$Specs = Join-Path $Root 'build\specs'
$DataSeparator = [IO.Path]::PathSeparator

if (-not (Test-Path $Python)) {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        py -3.12 -m venv $Venv
    }
    else {
        python -m venv $Venv
    }
}

if (-not $SkipInstall) {
    & $Python -m pip install --upgrade pip
    & $Python -m pip install -r (Join-Path $Root 'requirements-windows.txt')
}

New-Item -ItemType Directory -Force -Path $Work, $Specs | Out-Null

function Add-DataArgument {
    param(
        [string]$Source,
        [string]$Destination
    )

    $SourcePath = Join-Path $Root $Source
    return "$SourcePath$DataSeparator$Destination"
}

$Apps = @(
    @{
        Name = 'tool8_opencv_mosaic'
        Folder = 'tool8_opencv-python'
        Entry = 'tool8_opencv-python\8_opencv-python.py'
        Extra = @(
            '--add-data', (Add-DataArgument 'tool8_opencv-python\man_iamge.jpg' '.')
        )
    },
    @{
        Name = 'tool10_selenium_stock'
        Folder = 'tool10_selenium'
        Entry = 'tool10_selenium\10_selenium.py'
        Extra = @()
    },
    @{
        Name = 'projectB_docs_translator'
        Folder = 'projectB_docstranslator'
        Entry = 'projectB_docstranslator\main.py'
        Extra = @(
            '--add-data', (Add-DataArgument 'projectB_docstranslator\docs_example' 'docs_example')
        )
    },
    @{
        Name = 'projectC_certificate_maker'
        Folder = 'projectC_auto_certification_maker'
        Entry = 'projectC_auto_certification_maker\main.py'
        Extra = @(
            '--add-data', (Add-DataArgument 'projectC_auto_certification_maker\resource' 'resource')
        )
    },
    @{
        Name = 'projectE_video_mosaic'
        Folder = 'projectE_video_mosaic_app'
        Entry = 'projectE_video_mosaic_app\main.py'
        Extra = @(
            '--add-data', (Add-DataArgument 'projectE_video_mosaic_app\sample_video.mp4' '.')
        )
    },
    @{
        Name = 'projectF_wordcloud_webapp'
        Folder = 'projectF_wordcloud_webapp'
        Entry = 'projectF_wordcloud_webapp\flask_app.py'
        Extra = @(
            '--add-data', (Add-DataArgument 'projectF_wordcloud_webapp\templates' 'templates'),
            '--add-data', (Add-DataArgument 'projectF_wordcloud_webapp\static\apple_img.png' 'static'),
            '--collect-data', 'wordcloud'
        )
    }
)

Push-Location $Root
try {
    foreach ($App in $Apps) {
        $Dist = Join-Path (Join-Path $Root $App.Folder) 'dist'
        New-Item -ItemType Directory -Force -Path $Dist | Out-Null

        Write-Host "Building $($App.Name).exe -> $Dist"
        $Arguments = @(
            '-m', 'PyInstaller',
            '--noconfirm',
            '--clean',
            '--onefile',
            '--console',
            '--name', $App.Name,
            '--distpath', $Dist,
            '--workpath', $Work,
            '--specpath', $Specs
        ) + $App.Extra + @((Join-Path $Root $App.Entry))

        & $Python @Arguments
        if ($LASTEXITCODE -ne 0) {
            throw "$($App.Name) 빌드에 실패했습니다."
        }
    }
}
finally {
    Pop-Location
}

Write-Host ''
Write-Host '완료: 각 앱 폴더의 dist 디렉터리를 확인하세요.'
