from flask import Flask, render_template, request
from manga_translator import MangaTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if 'image' not in request.files:
        return render_template('index.html', error='No image provided')

    image = request.files['image']
    translator = MangaTranslator(image)
    translated_text = translator.translate()
    
    return render_template('index.html', original_text=translator.original_text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)