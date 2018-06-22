n= int (input("pick any positive numbers"))
import sys
for i in range(1,n+1):
   for j in range(1,n+1):
      k=i*j
      print (k, end=' ')
   print()