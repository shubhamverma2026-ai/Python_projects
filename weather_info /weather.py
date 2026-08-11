import requests

api_key = "a4922e0afb80c0e2876f53768f37c6df"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\n----- Weather Information -----")
    print("City:", city_name)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", weather)

else:
    print("Error:", response.status_code)
    print(response.text)
