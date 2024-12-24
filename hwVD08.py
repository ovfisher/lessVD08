from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('hwVD08.html', quote=quote)

def get_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    return "Не удалось получить цитату."

if __name__ == '__main__':
    app.run(debug=True)
