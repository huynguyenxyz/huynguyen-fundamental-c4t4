
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# for key in inventory.keys():
#     print (key,end = "\t")
pocket = ['strange berry','seashell','flint']
inventory["pocket"]=pocket
print (inventory)
inventory["backpack"].remove('dagger')
print (inventory)
inventory['gold']=500+50
print (inventory)
