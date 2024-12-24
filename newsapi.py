from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        # передаем информацию о погоде в index.html
        news = get_news()
    return render_template("index.html", weather=weather, news=news)

def get_weather(city):
   api_key = "0be9277feb0317dfd2e97b9467749ec4"
   #адрес, по которому мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   response = requests.get(url)
   return response.json()

def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', ['xxxxxxxxxxxxx'])

if __name__ == '__main__':
   app.run(debug=True)