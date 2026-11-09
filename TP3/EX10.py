chaine = input("Enter a number: ")

t = 0

for c in chaine :
    p = 1
    for i in range(1, int(c) + 1):
        p *= i
    t += p
if t == int(chaine):
    print("The number", chaine, "is a strong number.")
else:
    print("The number", chaine, "is not a strong number.")