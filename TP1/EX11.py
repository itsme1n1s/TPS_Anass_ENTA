import pyfiglet

Title = pyfiglet.figlet_format("Rectangle")
print(Title)

l = float(input("donne moi longeur de Rectangle: "))
L = float(input("Donne moi largeur: "))

A = l * L
P = (l + L) * 2

print(f"l' air de triangle est: {A:.2f} ", end="")
print(F"et perimetre de triange est: {P:.2f}")