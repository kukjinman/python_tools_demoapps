# python_tools_demoapps
python_tools_demoapps

## Windows EXE 빌드

PyInstaller는 실행 중인 운영체제용 프로그램만 만들 수 있으므로 Windows에서 빌드해야 합니다.
Windows 10/11에서 Python 3.12를 설치한 뒤 프로젝트 루트에서 아래 파일을 실행합니다.

```bat
build_windows.bat
```

빌드가 끝나면 `dist` 폴더에 다음 실행 파일이 생성됩니다.

- `tool8_opencv_mosaic.exe`
- `tool10_selenium_stock.exe`
- `projectB_docs_translator.exe`
- `projectC_certificate_maker.exe`
- `projectE_video_mosaic.exe`
- `projectF_wordcloud_webapp.exe`

GitHub 저장소의 **Actions > Build Windows EXE > Run workflow**에서도 빌드할 수 있습니다.
완료된 실행 파일은 `python-tools-demoapps-windows` artifact에서 내려받습니다.

Selenium 예제는 실행할 Windows PC에 Google Chrome이 설치되어 있어야 하며, 문서 번역기는
Google 번역 서비스에 접속할 수 있는 인터넷 연결이 필요합니다.
