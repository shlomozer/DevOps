import urllib.request, json

with urllib.request.urlopen ("https://free.currencyconverterapi.com/api/v5/convert?q=ILS_USD&compact=ultra&apiKey=4b36a7b9ba274115479d") as convert:
    CurrencyRate = json.loads(convert.read().decode())

ILS_USD = CurrencyRate['ILS_USD']

try:
    shekel = float(input("Enter shekel value:"))
    print("Result is:",float (shekel*ILS_USD))
    print("Thank you for using our converter")
except ValueError:
    print("invalid chice")

    