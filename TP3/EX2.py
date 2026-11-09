X = int(input("Enter a base number: "))
N = int(input("Enter a power number: "))
S = 1


for i in range(0 , N):
    S = S * X

print("The result is:", S)