import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), os.path.join(os.getcwd(), '.env'))
load_dotenv(dotenv_path)

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO').upper()
SENTIMENT_SERVER = os.getenv('SENTIMENT_SERVER', 'http://localhost:8501/v1/models/sentiment:predict')
