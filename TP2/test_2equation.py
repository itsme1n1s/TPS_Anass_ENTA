
import pyfiglet

Title = pyfiglet.print_figlet("2 Equation", colors="red")
while True:
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        break
    except ValueError:
        print("Invalid input. please enter a number.")

if a != 0:
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta **  0.5) / (2 * a)
        print(f"The solutions are x1 = {x1:2f} and x2 = {x2:2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"The solution is x = {x:2f}")
    else:
        print("aucune solution dans R")
else:
    if b!=0:
        print(f"solution de l'equation est", - b / c)
    else:
        if c!=0:
            print("aucune solution")
        else:
            print("Toute Les Valeurs de R sont des solution de l'equation")    