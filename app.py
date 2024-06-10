from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_api(city):
    API_KEY = '53d5494f281ec31c747c8328dd96712c'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/", methods=['POST','GET'])
def hello():
    if request.method == 'POST':
        city = str(request.form.get('txtciudad'))
        data = get_weather_api(city)
        if 'weather' in data:
            return render_template('index.html', context=data)
        else:
            return render_template('index.html', error_message='La ciudad ingresada no es correcta')
    else:
        return render_template('index.html')
    
@app.route('/cv')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)