# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Prompt the user to enter a temperature value and unit
temperature = float(input("Enter a temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert the temperature based on the unit
if unit.upper() == "C":
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {fahrenheit}°F")
elif unit.upper() == "F":
    celsius = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {celsius}°C")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")