print (f"(C+5)(B²-3AC)A²")
print ("__________________________________________________")
print (f"4A")



aVal= float (input("Inserte valor A aqui pls: "))
bVal= float (input("Inserte valor B aqui pls: "))
cVal= float (input("Inserte valor C aqui pls: "))

print ("Solo para confirmar tu ecuacion seria: ")
print (f"({cVal}+5)({bVal}²-3({aVal}*{cVal})){aVal}²")
print ("__________________________________________________")
print (f"4*{aVal}")

n1= cVal+5
n2= (bVal**2)-3*(aVal*cVal)
n3= aVal**2

r= (n1*n2*n3)/(4*aVal)

print (n1)
print (n2)
print (n3)


print ("Resultado: ",r)
#print ((cVal+5)(((bVal**2)-3)(aVal*cVal)))*(aVal**2)