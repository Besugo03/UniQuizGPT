from openai import OpenAI
import dotenv
import os
import requests

default_model = "gpt-4o-mini"

def load_envkeys() -> str: 
    """
    Returns the OpenAI API key from the .env file in string format.
    """
    # if the .env file is not found, the following line will raise an exception
    dotenv.load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise Exception("OpenAI API Key not found in .env file. Please insert OPENAI_API_KEY = 'your_key_here' in the .env file")
    return api_key

def print_models() -> None:
    """
    Prints the available models on the OpenAI API.
    """
    api_key = load_envkeys()

    # Set up the headers with the authorization token
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Make the GET request
    response = requests.get("https://api.openai.com/v1/models", headers=headers)
    # print(response.json())

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Print the list of models
        for model in data['data']:
            print(f"Model ID: {model['id']}")
            # print(f"Created: {model['created']}")
            # print(f"Owned by: {model['owned_by']}\n")
    else:
        print(f"Request failed with status code {response.status_code}")

client = OpenAI(api_key=load_envkeys())

# open the prompt.txt file and read the prompt
with open("prompt.txt", "r") as file:
    prompt = file.read()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful study assistant for a computer science student."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)