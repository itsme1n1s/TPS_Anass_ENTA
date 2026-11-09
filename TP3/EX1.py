N = int(input("enter a number: "))
S = 0
while N <= 0:
    print("Please enter a positive number.")
    N = int(input("enter a number: "))

for i in range(1, N + 1):
    S = S + 1 / i
print("The result is:", S)