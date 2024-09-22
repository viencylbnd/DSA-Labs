#Lab Assignment 1
#Submitted by: Viency E. Labanda
#Course, Year & Section: BSCpE 1-3
#Submitted to: Godofredo T. Avena
#Date Submitted: September 22, 2024

#1: Temperature Converter

def converttemp():
    temp = float(input("Enter temperature:"))
    
    forc_convert = input("Convert to Celsius or Fahrenheit? Type C or F only.")
    
    if forc_convert == 'C':
        result = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {result:.2f}°C")
    elif forc_convert == 'F':
        result = (temp* 9/5) + 32
        print(f"{temp}°C is equal to {result:.2f}°F")
    else:
        print("Error. Please type C or F only.")

converttemp()
