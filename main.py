import requests


def getCrypto():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()


cryptoResponse = getCrypto()
userInput = input("Enter your crypto currency: ")

for crypto in cryptoResponse:
    if crypto["currency"] == userInput:
        print(crypto["price"])
        break
