import sys
sys.path.append("lib/python3.12/site-packages")
import os
import requests

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

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

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
            translate_client = google_translate.Client()
            if isinstance(text, bytes):
                text = text.decode("utf-8")
            result = translate_client.translate(text, target_language=target_language)
            translation = result['translatedText']
        elif api == 'OpenAI':
            # Call OpenAI API
            data = {
                "model": "gpt-3.5-turbo",  # Adjust the model as necessary
                "messages": [
                    {"role": "user", "content": f"Translate the following text into {target_language}: '{text}'"}
                ]
            }

            headers = {
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)

            if response.status_code == 200:
                translation = response.json()['choices'][0]['message']['content']
            else:
                translation = f"Failed to translate text. Error: {response.text}"
    return render_template('home.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
