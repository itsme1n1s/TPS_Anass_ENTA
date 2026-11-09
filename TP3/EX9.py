chaine = input("Enter a string: ")
A = ""

for c in chaine :
    A = c + A

if A == chaine:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")