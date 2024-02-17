# Translation Flask App

This Flask application allows users to translate text between multiple languages using three different translation APIs: DeepL, Google Translate, and OpenAI. It's designed as a basic framework for experimenting with different translation services.

## Installation Instructions

### Prerequisites

- Python 3.x
- Pip
- Virtualenv (recommended)

### Setup

#### 1. Clone the Repository

Clone the project to your local machine using the following command:

```bash
git clone https://yourrepository.com/translation_flask_app.git
cd translation_flask_app
```

#### 2. Create and Activate a Virtual Environment

For macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```
python -m venv venv
venv\Scripts\activate
```

#### 3. Install Required Packages

Install Flask and the necessary libraries for the translation APIs:

```
pip install Flask google-cloud-translate deep-translator openai
```

You can also use the requirements.txt file with all dependencies.

```
pip install -r requirements.txt
```

#### 4. Configure API Keys

- **DeepL**: Sign up at [DeepL Pro](https://www.deepl.com/pro#developer) and obtain an API key. Place your API key in the `app.py` file.
- **Google Translate**: Follow the instructions at [Google Cloud Translation](https://cloud.google.com/translate/docs/setup) to set up a project and obtain a JSON credentials file. Reference the path to your JSON credentials in the `app.py` file.
- **OpenAI**: Obtain an API key by signing up at [OpenAI](https://openai.com/). Place your API key in the `app.py` file.

#### 5. Create a secret.py file

In the root of the project, create a file called `secret.py` and add your API keys like this:

```
OPENAI_API_KEY = 'your_openai_api_key'
DEEPL_API_KEY = 'your_deepl_api_key'
GOOGLE_APPLICATION_CREDENTIALS = 'path_to_your_google_credentials_json'
```

## Running the Application

### 1. Start the Flask App

Launch the application with Flask:

```
flask run
```

This will start the server on http://127.0.0.1:5000/.

### 2. Navigate to the Application

Open a web browser and access the application at http://127.0.0.1:5000/.

## Using the Application

- **Translate Text**: Enter the text you wish to translate, select the target language (e.g., `en` for English, `de` for German), choose the translation API, and click the "Translate" button.
- **Supported Languages**: The application supports translating into multiple languages, including English, Spanish, Arabic, and Hindi. Ensure the target language code is correctly entered.

## Sample Prompts for Translation

<details>
<summary><b>Medical Emergency</b>: "I need medical assistance immediately. I am experiencing severe chest pain and difficulty breathing."</summary>

- **Arabic**: "أحتاج إلى مساعدة طبية فورية. أعاني من ألم شديد في الصدر وصعوبة في التنفس."
- **Spanish**: "Necesito asistencia médica inmediatamente. Estoy experimentando un dolor severo en el pecho y dificultad para respirar."
- **Hindi**: "मुझे तुरंत चिकित्सा सहायता की आवश्यकता है। मैं गंभीर सीने में दर्द और सांस लेने में कठिनाई का अनुभव कर रहा हूँ।"

</details>

<details>
<summary><b>Physical Danger</b>: "I am in danger and need help. Someone is following me, and I fear for my safety."</summary>

- **Arabic**: "أنا في خطر وأحتاج إلى المساعدة. هناك شخص يتبعني وأنا خائف على سلامتي."
- **Spanish**: "Estoy en peligro y necesito ayuda. Alguien me está siguiendo y temo por mi seguridad."
- **Hindi**: "मैं खतरे में हूं और मुझे मदद की जरूरत है। कोई मुझे फॉलो कर रहा है और मुझे अपनी सुरक्षा का डर है।"

</details>

<details>
<summary><b>Lost or Stranded</b>: "I am lost and cannot find my way back. I need assistance to get to a safe location."</summary>

- **Arabic**: "أنا ضائع ولا أستطيع العثور على طريق العودة. أحتاج إلى مساعدة للوصول إلى مكان آمن."
- **Spanish**: "Estoy perdido y no puedo encontrar el camino de vuelta. Necesito ayuda para llegar a un lugar seguro."
- **Hindi**: "मैं खो गया हूं और वापस जाने का रास्ता नहीं पा रहा हूँ। मुझे किसी सुरक्षित स्थान पर जाने के लिए सहायता की आवश्यकता है।"

</details>

<details>
<summary><b>Natural Disaster</b>: "Affected by the earthquake, trapped under debris. Need rescue services immediately."</summary>

- **Arabic**: "تأثرت بالزلزال، محاصر تحت الأنقاض. بحاجة إلى خدمات الإنقاذ فوراً."
- **Spanish**: "Afectado por el terremoto, atrapado bajo los escombros. Necesito servicios de rescate de inmediato."
- **Hindi**: "भूकंप से प्रभावित, मलबे के नीचे फंसा हुआ। मुझे तुरंत बचाव सेव &#8203;``【oaicite:0】``&#8203;

Please replace the placeholder paths and API keys in the `app.py` file with your actual credentials before running the application.
