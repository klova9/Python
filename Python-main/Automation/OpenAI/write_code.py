import key
import requests
import argparse

api_endpoint = 'https://api.openai.com/v1/completions'
api_key = key.key

parser = argparse.ArgumentParser()
parser.add_argument('user_input', help='Code to write')
args = parser.parse_args()

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

request_data = {
    'model': 'text-davinci-003',
    'prompt': f'Write python script to {args.user_input}, Provide only code, no text',
    'max_tokens': 1000,
    'temperature': 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()['choices'][0]['text']
    with open('output.py', 'w+') as f:
        f.write(response_text)
        
else:
    print(f'Request failed with status code {str(response.status_code)}')