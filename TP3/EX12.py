number = int(input("Enter a number: "))
num = 0
while num < number:
    num += 1
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ", sep ="-") 
  