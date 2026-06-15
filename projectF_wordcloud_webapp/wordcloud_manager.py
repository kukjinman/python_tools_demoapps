import numpy as np
from PIL import Image
from wordcloud import WordCloud

from runtime_paths import output_path, resource_path

words = []
static_dir = output_path('wordcloud_webapp_data', 'static')
static_dir.mkdir(parents=True, exist_ok=True)
masking_image = np.array(Image.open(resource_path('static', 'apple_img.png')))

#5 add_word 함수
def add_word(new_word):
    # print(words)
    words.append(str(new_word))
    text = ' '.join(words)
    wordcloud = WordCloud(mask = masking_image, background_color='lightgrey', include_numbers=True).generate(text)

    #6 static 폴더에 wordcloud.png 저장
    wordcloud.to_file(static_dir / 'wordcloud.png')
