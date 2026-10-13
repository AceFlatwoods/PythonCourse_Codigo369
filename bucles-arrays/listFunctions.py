# Lists introduction, not much else

array = [1.67, 2, 3, -23, 7, "Lorem", "Ipsum", "Ipsum"]
array2 = [5, 4, 234, 2, 1]
array2.sort(reverse=True) # Sorts it and reverses it, highest to lowest, simple as
print(array2) 

array.reverse() # Reverses it
print(array)

print(len(array)) # Gets how many values the array has
array.append(703) # Adds this number to the original array
array.insert(1,888) # Adds this number between the 0 and 1 position, essentially taking over the number 1 position
array.extend([5,88,True,100]) #Adds these all to the end of the array
print("Lorem" in array) # Search for the word in the array, it's a True/False print
print(array.index("Lorem")) # Searches for number of position of said value
print(array.count("Ipsum"))
array.remove(1.67) # Removes said value
print(array)

#You can also add an array to another, but well, no need to put it here, you can picture it, it's just concatenation