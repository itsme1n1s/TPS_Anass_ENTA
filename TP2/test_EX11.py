num = int(input("donne moi le numero :"))

if num < 0 and num > 6 :
    print("La valeur est en dehors de l'intervalle")
else : 
    if num == 0 :
        print("Dimanche")
    if num == 1 :
        print("Lundi")
    if num == 2 :
        print("Mardi")
    if num == 3 :
        print("Mercredi")
    if num == 4 :
        print("Jeudi")
    if num == 5 :
        print("Vendredi")
    if num == 6 :
        print("Samedi")