#2 numeros, el programa dira cual de los dos es par, si los dos lo son lo dira
num1 = int(input ("Inserte numero: "))
num2 = int(input ("Inserte numero: "))

r1= num1%2
r2= num2%2
print(f"Haciendo la formula el primero queda como:         {r1}     y el segundo como:     {r2}")

if ((r1==0) and (r2==1)):
    print ("El primer numero que ingresaste es par, el otro no ig")

elif ((r1==1) and (r2==0)):
    print ("El segundo numero que ingresaste es par, el otro no ig")

elif ((r1==0) and (r2==0)):
    print ("Los dos numeros son pares")

else:
    print("Ninguno es par ig")