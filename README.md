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

- **Medical Emergency**: "I need medical assistance immediately. I am experiencing severe chest pain and difficulty breathing."
- **Physical Danger**: "I am in danger and need help. Someone is following me, and I fear for my safety."
- **Lost or Stranded**: "I am lost and cannot find my way back. I need assistance to get to a safe location."
- **Natural Disaster**: "Affected by the earthquake, trapped under debris. Need rescue services immediately."

Please replace the placeholder paths and API keys in the `app.py` file with your actual credentials before running the application.
