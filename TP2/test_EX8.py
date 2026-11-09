a = float(input("donne moi le numero 1: "))
b = float(input("donne moi le numero 2: "))

if a > b :
    b = float(input("donne moi le numero 3:"))
    if a > b :
        b = float(input("donne moi le numero 4: "))
        if a > b :
            print("le numero le plus grand est :", a)
        else :
            print("le numero le plus grand est :", b)
else :
    a = float(input("donne moi le numero 3:"))
    if b > a : 
            a = float(input("donne moi le numero 4:"))
            if b > a :
                print("le numero le plus grand est :", b)
            else :
                print("le numero le plus grand est :", a)
    else :
         b = float(input("donne moi le numero 4:"))
         if b > a :
                print("le numero le plus grand est :", b)
         else :
                print("le numero le plus grand est :", a)
