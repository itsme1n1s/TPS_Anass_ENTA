lettre = input("donne moi la lettre")

cons = {"B", "C", "D", "F","J","G","K","L","M","N","P", "Q", "R","S","T","V","W","X","Z","b","c","d","f","j","g","k","l","m","n","P","q","r","s","t","v","w","x","z" }
vo = {"a", "o", "u", "e", "y", "i" ,"A", "O", "U", "E", "Y", "I"}

if lettre in cons :
    print("c'est un consonne")
elif lettre in vo :
    print("c'est un voyelle")
else :
    print("Mchi b7alk la nsdk dayrlk wa7d")