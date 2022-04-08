#calculater
''' 
x = input("What's x?")
y = input("What's y?")
z = int(x) + int(y)
print(z)
'''
#same as above
'''x = int(input("What's x?"))
y = int(input("What's y?"))

print(x + y)'''

#float we can write decimal number
'''
x = float(input("What's x?"))
y = float(input("What's y?"))

print(x + y)
'''

#not show decimal and show around number
x = float(input("What's x?"))
y = float(input("What's y?"))
z = round(x + y)
print(z)#this show in normal mathed like 1000
print(f"{z:,}") #this show in proper style like 1,000
