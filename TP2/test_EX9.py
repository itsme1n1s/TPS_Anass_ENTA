caracter = input("donne moi le caractere")

maj = {
    "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"
}

mun = {
    "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"
}

if caracter in maj :
    print("Majuscule")
elif caracter in mun :
    print("Minuscule")
else:
    print("Autre caractere")