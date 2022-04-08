#str
#Ask or input name then show other thing
"""
name = input("input your name")
print ("hello,")
print (name)
"""
#same as above
'''
name = input("input your name")
print ("hello,", end="")
print (name)
'''
'''
name = input("input your name")
#remove extra whitespace from str anf capitalize user it capitial the code
#we can write on one line- 
name = name.strip().title()
print (f"hello {name}")
'''