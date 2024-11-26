
for i in range(5):
    print("Python")

lim = int(input("Ingresa el límite: "))
i = 1
while i <= lim:
    if i % 2 == 0:  
        print(f"{i} es par")
    elif i % 3 == 0:  
        print(f"{i} es múltiplo de 3")
    else:
        print(f"{i} no es par ni múltiplo de 3")
    i += 1

lim = int(input("Ingresa otro límite: "))
i = 0
while i <= lim:
    if i == 0:
        print(f"{i} es el número cero")
    elif i % 2 == 0:  
        print(f"{i} es par")
    elif i % 5 == 0:  
        print(f"{i} es múltiplo de 5")
    else:
        print(f"{i} no es ni par ni múltiplo de 5")
    i += 1


