from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# REPLACE THIS with your actual Make.com Webhook URL
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/nxdnq20l2vmcchnqq2jw7iyhil7jcgpf"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/lead', methods=['POST'])
def handle_lead():
    data = request.json
    # The JSON now contains 'event_type' (e.g., SME_INVESTMENT)
    print(f"Processing Event: {data['event_type']}")

    response = requests.post(MAKE_WEBHOOK_URL, json=data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)