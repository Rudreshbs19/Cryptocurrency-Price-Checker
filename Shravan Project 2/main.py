import requests
import csv

def search_crypto():

    try:

        coin = input("Enter Cryptocurrency Name: ").lower().strip()

        if coin == "":
            print("Please enter a cryptocurrency name!")
            return

        url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin}"

        response = requests.get(url, timeout=10)

        data = response.json()

        if len(data) > 0:

            print("\n")
            print("Name:", data[0]["name"])
            print("Symbol:", data[0]["symbol"].upper())
            print("Price: $", data[0]["current_price"])
            print("Market Cap Rank:", data[0]["market_cap_rank"])
            print("24H Change:", data[0]["price_change_percentage_24h"], "%")
            save_to_csv(
                data[0]["name"],
                data[0]["symbol"].upper(),
                data[0]["current_price"],
                data[0]["market_cap_rank"]
                )
        else:

            print("Cryptocurrency not found!")

    except requests.exceptions.RequestException:

        print("Unable to connect to CoinGecko. Check your internet connection.")

    except Exception as e:

        print("Error:", e)
        
       


def top_10_crypto():

    try:

        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"

        response = requests.get(url, timeout=10)

        data = response.json()

        print("\n")
        print("TOP 10 CRYPTOCURRENCIES")
        print("-" * 50)

        for coin in data:

            print(
                coin["market_cap_rank"],
                coin["name"],
                "$" + str(coin["current_price"])
            )

    except requests.exceptions.RequestException:

        print("Unable to connect to CoinGecko. Check your internet connection.")

    except Exception as e:

        print("Error:", e)
        
def save_to_csv(name, symbol, price, rank):

    with open("crypto_data.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [name, symbol, price, rank]
        )

    print("Data saved to crypto_data.csv")

while True:

    print("\n")
    print("=" * 35)
    print(" CRYPTO PRICE TRACKER ")
    print("=" * 35)

    print("1. Search Cryptocurrency")
    print("2. Top 10 Cryptocurrencies")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        search_crypto()

    elif choice == "2":

        top_10_crypto()

    elif choice == "3":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")