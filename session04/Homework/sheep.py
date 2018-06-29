size = [5,7,300,90,24,50,75]
print('''Hello my name is a and these are my sheeps' size''')
print (size)
max_size = max(size)
print("My biggest sheep has size {0}, let's shear it".format(max_size))
size[size.index(max_size)] = 8
print ("After shearing, here is my flock")
print(size)

for j in range (4):
    print("Month {0}".format(j+1))
    print("One month passed, here is my flock")
    for i in range (len (size)):
        size[i]+=50
    print(size)
    max_size2 = max (size)
    print("My biggest sheep has size {0}, let's shear it".format(max_size2))
    size[size.index(max_size2)] = 8
    print ("after shearing, here is my flock")
    print(size)
nor = 0
for i in range (7):
    nor = size[i] + nor
print ("My flock has size in total: {0}".format(nor))
print("I will have:",nor * 2,"$")

    
    

    
        

