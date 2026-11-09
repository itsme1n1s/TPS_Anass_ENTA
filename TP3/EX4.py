N = int(input("Enter a number: "))
while N <= 0:
    print("Please enter a positive number.")
    N = int(input("Enter a number: "))
S = 0
for i in range(1, int(N/ 2) + 1):
        if N % i == 0:
            S = S + i
if S == N:
    print("parfait")
else:
    print("non parfait")