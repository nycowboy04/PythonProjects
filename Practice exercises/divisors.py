a = int(input("Please enter a number: "))

x = range(2, a)

for item in x:
    if a%item == 0:
        print(item, "is a divisor of", a)
