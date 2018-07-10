number = int(input("Enter a number"))
a = 0

for i in range (1, numb):
    if number % i == 0:
        a += i
if a == numb:
    print("{0} is a perfect number".format(numb))
else:
    print("{0} is a not perfect number".format(numb))
