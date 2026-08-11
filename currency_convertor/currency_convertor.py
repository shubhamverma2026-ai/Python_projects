import requests

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD/INR/EUR): ").upper()
to_currency = input("To currency (USD/INR/EUR): ").upper()

url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    result = data["rates"][to_currency]

    print("\n----- Currency Converter -----")
    print("Amount:", amount, from_currency)
    print("Converted:", result, to_currency)

else:
    print("Something went wrong!")
