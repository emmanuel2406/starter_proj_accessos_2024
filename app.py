from flask import Flask, request, render_template
from google.cloud import translate_v2 as google_translate
from deep_translator import GoogleTranslator as deep_google_translate
from deep_translator import DeepL
from googletrans import Translator, constants
import openai
from secret import OPENAI_API_KEY, DEEPL_API_KEY, GOOGLE_APPLICATION_CREDENTIALS
from google.oauth2 import service_account

app = Flask(__name__)

# Your work will be in this file. Look at README.md for more information on how to set up the API keys.
# Don't forget to create a secret.py file with your keys. 

openai.api_key = OPENAI_API_KEY

@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ""
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']
        api = request.form['api']

        if api == 'DeepL':
            # Call DeepL API
            translation = "REPLACE WITH CODE"
        elif api == 'Google':
            # Call Cloud Translation API from Google
            translation = "REPLACE WITH CODE"
        elif api == 'OpenAI':
            # Call OpenAI API
            translation = "REPLACE WITH CODE"

    return render_template('home.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
