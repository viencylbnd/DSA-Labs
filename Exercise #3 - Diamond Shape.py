#Lab Assignment 1
#Submitted by: Viency E. Labanda
#Course, Year & Section: BSCpE 1-3
#Submitted to: Godofredo T. Avena
#Date Submitted: September 22, 2024

#3: Diamond Shape



def print_diamond():
    n_width = int(input("To determine the width of the diamond, please enter an odd number: "))

    if n_width % 2 == 0:
        return "The number you entered is an even number. Please try again."
 
    for i in range(n_width // 2 + 1):
        print(' ' * (n_width // 2 - i) + '*' * (2 * i + 1))
 
    for i in range(n_width // 2 - 1, -1, -1):
        print(' ' * (n_width // 2 - i) + '*' * (2 * i + 1))

diamond = print_diamond()
print(diamond)
