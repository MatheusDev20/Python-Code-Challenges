from app.weather import weather_bp
from flask import request as current_request, render_template
from app.weather.open_weather import GetWeather

@weather_bp.route('/', methods=['GET', 'POST'])
def show_weather():
    temp = None
    error = None
    if current_request.method == 'POST':
        status, weather = GetWeather.get_city_weather(current_request.form['city'])
        print(status)
        if status != 200:
            error = weather['message']

        else:
            temp = weather['main']['temp']
    
    template_context = dict(weather=temp, err=error)
    return render_template('weather.html', **template_context)
