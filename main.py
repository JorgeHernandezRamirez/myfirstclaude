from flask import Flask, request, jsonify
import anthropic
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask app by Jorge - updated again!'

@app.route('/ask', methods=['POST'])
def ask_claude():
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({'error': 'Message is required'}), 400

        # Initialize Anthropic client
        client = anthropic.Anthropic(
            api_key=os.environ.get('ANTHROPIC_API_KEY')
        )

        # Call Claude API
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": message}
            ]
        )

        return jsonify({
            'response': response.content[0].text
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
