from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
# Decorator
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}

if __name__ == "__main__":
    app.run(debug=True)
# app.run only when main.py is executed directly
# But if we just import this script, for example to use the functions, it will NOT run app