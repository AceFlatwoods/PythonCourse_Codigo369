n1= float (input("Inserte precio: "))
n2= int (input("Inserte el descuento que se le aplicara: "))
disc= (n1/100)*n2
pricend= n1-disc

print (f"Su descuento es de: {disc}")
print (f"Also lo que tienes que pagar es: {pricend}")