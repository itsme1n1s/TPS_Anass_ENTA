chaine = input("Enter a string: ")
lettre = input("Enter a letter: ")
count = 0
s = ""
for c in chaine :
    if c == lettre:
        count += 1
print("The letter", lettre, "appears", count, "times in the string.")