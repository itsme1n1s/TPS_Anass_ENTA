nom1 = input("donne moi le nom de persone 1 :") #{}
age1 = int(input(f"donne moi l'age de {nom1} :"))
nom2 = input("donne moi le nom de persone 2 :")
age2 = int(input(f"donne moi l'age de {nom2} :"))
nom3 = input("donne moi le nom de persone 3 :") 
age3 = int(input(f"donne moi l'age de {nom3} :"))

if age1 > age2 :
    if age1 > age3 :
        print("le plus agee est:", nom1)
    else :
        print("le plus agee est:", nom3)
elif age2 == age1 == age3 :
    print("ils sont tous les 3 egaux")
else: 
    if age2 > age3 :
        print("le plus agee est:", nom2)
    else : 
        print("le plus agee est:", nom3)