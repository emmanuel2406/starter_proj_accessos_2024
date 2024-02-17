from flask import Flask, request, render_template
from google.cloud import translate_v2 as google_translate
from deep_translator import GoogleTranslator as deep_google_translate
import openai
from secret import OPENAI_API_KEY, DEEPL_API_KEY, GOOGLE_APPLICATION_CREDENTIALS

app = Flask(__name__)

openai.api_key = OPENAI_API_KEY

@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ""
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']
        api = request.form['api']

        if api == 'DeepL':
            from deep_translator import DeepL
            translator = DeepL(api_key=DEEPL_API_KEY)
            translation = translator.translate(text, target_language=target_language)
        elif api == 'Google':
            translator = google_translate.Client()
            result = translator.translate(text, target_language=target_language)
            translation = result['translatedText']
        elif api == 'OpenAI':
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=f"Translate the following text to {target_language}: {text}",
                temperature=0.3,
                max_tokens=60
            )
            translation = response.choices[0].text.strip()

    return render_template('home.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
