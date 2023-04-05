from flask import Flask, render_template, request
import requests

API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    text = request.form['text']
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    sentiments = response.json()[0]
    sentiments.sort(key=lambda x: x['score'], reverse=True)
    sentiment_label = sentiments[0]['label']
    return render_template('result.html', sentiment=sentiment_label)

if __name__ == '__main__':
    app.run()
