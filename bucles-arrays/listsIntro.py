# Just an intro to lists

A = {1,2,3,4}
B = {2,3,5,6}
C = {3,4,6,7} # There if usage is needed, didn't really use it

print(A==B) #See if they are the same
print(A|B) # Makes these two whole again (Combines them and does not repeat values)
print(A&B) # Intersects them, anything that's the same, it outputs, in this case 2 and 3
print(A-B) # Elements that pertain to A but not to B, 1 and 4 in this case, everything else is reduced to nothing