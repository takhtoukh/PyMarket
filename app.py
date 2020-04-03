from flask import Flask, render_template, request
import market

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("form.html")


@app.route('/resultat', methods=['POST'])
def resultat():
    result = request.form
    latitude = result['latitude']
    longitude = result['longitude']
    print(latitude)
    markets = market.nearest_markets(float(latitude), float(longitude))
    return render_template("resultat.html", markets=markets)


if __name__ == "__main__":
    app.run()
