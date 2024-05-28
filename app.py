from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather_api(city):
    API_KEY = '53d5494f281ec31c747c8328dd96712c'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/")
def index():
    data = (get_weather_api('Guayaquil'))
    return render_template('index.html',context=data)

if __name__ == '__main__':
    app.run(debug=True)