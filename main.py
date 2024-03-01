from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
# Decorator
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def get_temperature(station, date):
    try:
        file_name = f"data/TG_STAID{str(station).zfill(6)}.txt"
        # See jupyter previous code
        df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
        # have in jupyter
        temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
        return {"station": station,
                "date": date,
                "temperature": temperature}
    except FileNotFoundError:
        return {"station": "No Such Station",
                "date": date,
                "temperature": "N/A"}

if __name__ == "__main__":
    app.run(debug=True)
# app.run only when main.py is executed directly
# But if we just import this script, for example to use the functions, it will NOT run app