number = int(input("Enter a number: "))

for i in range(1, number + 1, 2):
    print(" " * (number - i) + "*" * (2 * i - 1))
