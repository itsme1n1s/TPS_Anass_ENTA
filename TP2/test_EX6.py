a = float(input("Donne moi numero A: "))
b = float(input("Donne moi numero B: "))

if a > 0 and b > 0:
    check = a % b
    if check == 0 :
        print("A divisible par B")
    else:
        print("A n'est pas divisible par B")