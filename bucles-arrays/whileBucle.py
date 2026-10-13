# While bucle
# Remember when stuff like this was able to land you a job? Yeah, me neither, I wish

import math
number = int(input("Write a number: "))

while number<0:
    print("Please add a positive number my good fellow: ")
    number = int(input("Write a number again please: "))

print(f"The result of the square root is: {math.sqrt(number):.2f}") # :.2f it's just to only show 2 decimals and not the entire thing, readability