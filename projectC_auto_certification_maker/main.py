from pyxl_manager import read_certification_list
from docx_manager import create_certificates
from runtime_paths import output_path, resource_path

file_path = resource_path('resource', '파이썬수료증리스트.xlsx')
template_file_path = resource_path('resource', '수료증_template.docx')
output_directory = output_path('output')

#0 수료증 인원 정보 리스트를 생성
certification_list = read_certification_list(file_path)
print(certification_list)

#3 수료증 생성
create_certificates(certification_list, template_file_path, output_directory)
print(f'완료: {output_directory}')
