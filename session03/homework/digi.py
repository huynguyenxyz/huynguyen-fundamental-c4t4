count = 0
n = int(input("pls insert a number."))
if n==0:
    print("it", "has",1, "digit(s)")
while n>0:
    n = n//10
    count+=1
print ("it", "has", count, "digit(s)" )


