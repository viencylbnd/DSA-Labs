#Lab Assignment 1
#Submitted by: Viency E. Labanda
#Course, Year & Section: BSCpE 1-3
#Submitted to: Godofredo T. Avena
#Date Submitted: September 22, 2024

#2: Ohm's Law Calculator

def calculate_vir():
    calc = int(input("What do you want to calculate? V-Voltage, I-Current, or R-Resistance? "))
    
    if calc == 'V':
        I = float(input("Enter Current (I): "))
        R = float(input("Enter Resistance (R): "))
        V = I * R
        print(f"{V:.2f} Volts")

    elif calc == 'I':
        V = float(input("Enter Voltage (V): "))
        I = float(input("Enter Current (I): "))
        if I == 0:
            print("Current can't be zero")
        else:
            I = V / R
            print(f"{I:.2f} Ohms")

    elif calc == 'R':
        V = float(input("Enter Voltage (V): "))
        R = float(input("Enter Resistance (R): "))
        if R == 0:
            print("Current can't be zero.")
        else:
            R = V / I
            print(f"{R:.2f} Amperes")

    else:
        print("Try Again. Choose between V,I,& R only.")

calculate_vir()
