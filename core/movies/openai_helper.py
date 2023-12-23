# This file initializes the .env file and gets the api key
import openai
from dotenv import load_dotenv
import os

def initialize_openai():
    try:
        # Attempt to load environment variables from .env file
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))  # Navigate up two directories
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
    except FileNotFoundError:
        # Handle the case when .env file is missing
        print(".env file not found. Environment variables will not be loaded.")

    # Set the OpenAI API key with a default value if .env is missing or key is not available
    openai.api_key = os.getenv('OPENAI_API_KEY', 'notavalidapikey')