import cv2

from runtime_paths import output_path, resource_path

#1 frontalface 정면 얼굴 인식용 필터
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#2 이미지 읽기
image = cv2.imread(str(resource_path('man_iamge.jpg')))
if image is None:
    raise FileNotFoundError('man_iamge.jpg 파일을 읽을 수 없습니다.')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#3 얼굴 검출
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#4 모자이크 처리
for (x, y, w, h) in faces:
    face_region = image[y:y+h, x:x+w]
    face_region = cv2.resize(face_region, (w//10, h//10))
    face_region = cv2.resize(face_region, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = face_region

#5 결과 이미지 저장
result_path = output_path('mosaic_image.jpg')
cv2.imwrite(str(result_path), image)
print(f'완료: {result_path}')
