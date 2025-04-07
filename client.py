import openai
import os

# adding this for reading .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

print(os.getenv('OPENAI_API_KEY'))

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()
model="gpt-4o-mini"