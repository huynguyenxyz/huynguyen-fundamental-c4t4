
user = input("Username:")

if user == "abcxyz" :
    import getpass
    code =input("Password:")
    print (code)
    
    if code == "123":
        print("welcome") 
    else:
        print("wrong password")
else:
    
    print("fail login")