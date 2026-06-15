import threading
import webbrowser

from qrcode_manager import generate_qrcode
from flask import Flask, request, render_template, url_for
from runtime_paths import output_path, resource_path
from wordcloud_manager import add_word

static_dir = output_path('wordcloud_webapp_data', 'static')

#0 QR코드 생성
generate_qrcode("http://127.0.0.1:5000/", static_dir)

#3 Flask 앱 생성 및 실행
app = Flask(
    __name__,
    template_folder=str(resource_path('templates')),
    static_folder=str(static_dir),
    static_url_path='/static',
)


@app.route('/', methods=['GET', 'POST'])
def root_page():
    wordcloud_image = None
    if request.method == 'POST':
        word_input = request.form.get('word_input')

        #4 wordcloud_manager의 add_word 함수 호출
        add_word(word_input)
        wordcloud_image = url_for('static', filename='wordcloud.png')

    return render_template('mainpage.html', wordcloud_image=wordcloud_image)


if __name__ == '__main__':
    threading.Timer(1.0, lambda: webbrowser.open('http://127.0.0.1:5000/')).start()
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
