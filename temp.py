from flask import Flask, render_template, request
import requests # Needed for API use

app = Flask(__name__)
# Must have html files under templates directory to work
@app.route('/temperature', methods=['POST'])
def temperature():
    # Get the Form Value
    city = request.form['city']
    # api.openweathermap.org/data/2.5/weather?q={city name},{country code}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'ca'+'&appid=19438334675f7a4d72fd9bc77cf7c1a3')
    #json_object = r.text
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    # Kelvin Conversion to Farenheit
    temp_f = (temp_k - 273.15) * 1.8 + 32
    #return json_object
    #return render_template('temperature.html')
    return render_template('temperature.html', temp=temp_f)
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# My API Key 19438334675f7a4d72fd9bc77cf7c1a3
# http://openweathermap.org/current
