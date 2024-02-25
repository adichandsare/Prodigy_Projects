def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")
    temperature = float(input("Enter temperature value: "))
    unit = input("Enter unit of measurement (Celsius/C, Fahrenheit/F, Kelvin/K): ").upper()

    if unit == "C" or unit == "CELSIUS":
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit and {kelvin} Kelvin.")
    elif unit == "F" or unit == "FAHRENHEIT":
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius and {kelvin} Kelvin.")
    elif unit == "K" or unit == "KELVIN":
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin is equal to {celsius} Celsius and {fahrenheit} Fahrenheit.")
    else:
        print("Invalid unit of measurement.")

if __name__ == "__main__":
    main()
