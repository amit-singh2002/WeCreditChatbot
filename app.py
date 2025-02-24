from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')  # Use environment variable for security

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Call OpenAI's API to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    bot_message = response['choices'][0]['message']['content']
    return jsonify({"response": bot_message})

if __name__ == '__main__':
    app.run(debug=True)
