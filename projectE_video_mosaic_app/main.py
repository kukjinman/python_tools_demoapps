from opencv_manager import VideoMosaic
from runtime_paths import output_path, resource_path

video_path = resource_path('sample_video.mp4')
result_path = output_path('output_video.avi')

#0 VideoMosaic 클래스 객체 생성
video_mosaic = VideoMosaic(str(video_path), str(result_path))

#2 make_mosaic_video 함수 호출
video_mosaic.make_mosaic_video()
print(f'완료: {result_path}')
