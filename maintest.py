from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    crypto = None
    error = None

    if request.method == "POST":

        coin = request.form["coin"].lower().strip()

        if coin == "":
            error = "Please enter a cryptocurrency."

        else:

            url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}"

            response = requests.get(url)

            data = response.json()

            if len(data) > 0:

                crypto = {
                    "name": data[0]["name"],
                    "symbol": data[0]["symbol"].upper(),
                    "price": data[0]["current_price"],
                    "rank": data[0]["market_cap_rank"],
                    "change": data[0]["price_change_percentage_24h"],
                    "image": data[0]["image"]
                }

            else:

                error = "Cryptocurrency not found."

    return render_template(
        "index.html",
        crypto=crypto,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)