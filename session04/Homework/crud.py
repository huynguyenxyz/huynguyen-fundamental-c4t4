item = ["T - shirt","Sweater"]
asking = True
while asking:
    n = input("Welcome to our shop, what do you want (C,R,U,D)").lower()

    if n == "c":
        print(*item, sep = ", ")
    elif n == "r":
        new = input("Enter new item:")
        item.append (new)
        print(*item, sep = ", ")
    elif n == "u":
        pos = int( input("choose a position"))
        change = input( "enter new item")
        item[pos-1] = change
        print (*item, sep = ", ")
    elif n == "d":
        posi = int(input("delete position"))
        
        del item[posi-1]
        print(*item, sep = ", ")
    else:
        asking = False







