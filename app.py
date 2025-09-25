from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "be12c6a43132ec6ea38b2dead6e29ac8"  # replace with your real key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        if response.get("main"):
            weather_data = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"].title(),
                "icon": response["weather"][0]["icon"]
            }
        else:
            weather_data = {"error": "City not found!"}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
