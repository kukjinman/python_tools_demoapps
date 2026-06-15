#0 docx_manager, trans_manager 모듈 가져오기
from docx_manager import read_docx_files
from docx_manager import write_docx_files
from runtime_paths import output_path, resource_path
from trans_manager import translate_contents

input_directory = resource_path('docs_example')
output_directory = output_path('output')

#1 input_directory의 파일 순회
for docx_path in sorted(input_directory.glob('*.docx')):
    print(f"docx_file: {docx_path.name}")
    cur_data = read_docx_files(docx_path)
    print(f"cur_data: {cur_data}")
    result = translate_contents(cur_data)
    print(f"result: {result}")
    write_docx_files(result, output_directory, docx_path.name)

print(f"완료: {output_directory}")
