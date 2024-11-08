from flask import Flask, render_template
import requests

api_key='df6949058d174f7392094c0526cf93e5'
url =f'https://newsapi.org/v2/top-headlines?apiKey={api_key}&q=business'

app = Flask(__name__)
@app.route('/')
def home():
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    return render_template('index.html',
                           articles=articles)

if __name__ == '__main__':
    app.run(debug=True)