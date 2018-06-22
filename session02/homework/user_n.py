factorial=1
n = float(input("what is your number?"))
 
if n < 0:
    print("Factorial does not exist for negative numbers")
    print("Positive numbers only, please.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1,n+1):
        factorial = factorial*i
    print("The factorial of", n, "is", factorial)
    