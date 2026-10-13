#3 numeros, te dire cual es el mayor
num1 = int(input ("Inserte numero 1: "))
num2 = int(input ("Inserte numero 2: "))
num3 = int(input ("Inserte numero 3: "))

if ((num1>=num2) and (num1>=num3)):
    print (f"El numero mayor es el primero: {num1}")

elif ((num2>=num1) and (num2>=num3)):
    print (f"El numero mayor es el segundo: {num2}")

elif ((num3>=num2) and (num3>=num1)):
    print (f"El numero mayor es el tercero: {num3}")

else:
    print("Yeah idk, todos son par ig")