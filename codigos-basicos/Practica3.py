#Solo aprendi a importar math yyy limitar el numero de decimales + redondear el numero
import math
pi=math.pi #Sip, para mandar a llamar cosas de un paquete es lo mismo "nombredepaquete.cosa"
radio= float(input("Inserta radio: "))

radio=pi*(radio**2)
area=2*pi*radio

print (f"Area be like: {area:.3f}") #La f redondea el numero, el numero antes de esta es el numero de decimales que quieres, tambien los redondea al valor int mas cercano
print (f"Radio be like: {radio:.1f}") 