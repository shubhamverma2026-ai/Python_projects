temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif unit == "F":
    celsius = (temperature - 32) * 5/9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid unit.")
