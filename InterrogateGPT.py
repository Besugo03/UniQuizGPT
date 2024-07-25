import openai
import dotenv
import os

# if the .env file is not found, the following line will raise an exception
dotenv.load_dotenv()
if os.getenv("OPENAI_API_KEY") is None:
    raise Exception("OpenAI API Key not found in .env file. Please insert OPENAI_API_KEY = 'your_key_here' in the .env file")
print(os.getenv("OPENAI_API_KEY"))
