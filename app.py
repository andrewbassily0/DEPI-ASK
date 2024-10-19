from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('input')
    logging.debug(f'User input: {user_input}')
    
    url = "https://infinite-gpt.p.rapidapi.com/infinite-gpt"  # Ensure this is the correct endpoint
    headers = {
        "content-type": "application/json",
        "x-rapidapi-key": os.getenv('RAPIDAPI_KEY'),
        "x-rapidapi-host": "infinite-gpt.p.rapidapi.com"
    }
    
    # Update the payload to use 'query' instead of 'prompt'
    payload = {
        "query": user_input,  # Changed from 'prompt' to 'query'
        "max_tokens": 150  # Adjust as needed
    }

    logging.debug(f'Sending request to RapidAPI: {payload}')
    response = requests.post(url, json=payload, headers=headers)

    logging.debug(f'RapidAPI response: {response.status_code} {response.text}')

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to get response"}), response.status_code
    
if __name__ == '__main__':
    app.run(debug=True)
