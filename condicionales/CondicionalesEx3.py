#Tienes 2000 pesotes, el programa hace lo que dice que hace hasta que digas 4

dineros=2000

print("1.- Ingresar dinero")
print("2.- Retirar dinero")
print("3.- Checar tu balance")
print("4.- Salir")

opcion = int(input ("Que te gustaria hacer papu? "))
while opcion!=4:
    if opcion==1:
        ingreso = int(input("Cuanto dinero quieres ingresar? "))
        dineros+=ingreso
        print(f"Nuevo saldo: {dineros}")
        

    elif opcion==2:
        retiro = int(input("Cuanto dinero quieres retirar papu? "))
        if retiro>dineros:
            print("Equisde te falta dinero, imagine, especificamente te faltan: $", retiro-dineros, " pesotes")
        else:
            dineros-=retiro
            print(f"Nuevo saldo: {dineros}")
    elif opcion==3:
        print(f"Saldo rn fr fr: {dineros}")

    elif opcion==4:
        print("Welp, saliste del programa ig")
        