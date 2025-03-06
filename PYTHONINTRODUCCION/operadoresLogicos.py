valor = type(True)
print(valor) # <calss 'boo'l>
bool(1)
print(bool(1)) # True
print(bool(0)) # False
print(bool(2)) # True
print(bool(-1)) # True
print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool('')) # False
print(bool(' ')) # True
print(bool('Hola')) # True
print(bool([])) # False
print(bool([1,2,3])) # True
print(bool({})) # False
print(bool({'a':1})) # True

print(True + True) #True 
print(True + False) #False
print(False + False) #False 
print(False + True) #False
print(True and True) #True
print(True and False) #False 
print(False and False) #False 
print(False and True) #False 
print("-------------------------") #False
print(True or True) #True
print(True or False) #True
print(False or False) #FALSE
print(False or True) #True
print("-------------------------")
print(1 == 1) #True
print(1 == 2) #False 
print(1 != 1) #False
print(1 != 2) #True
print(1 < 2) #True
print(1 > 2) #False
print(1 <= 2) #true
print(1 >= 2) #False
