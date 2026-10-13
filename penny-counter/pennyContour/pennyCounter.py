# Penny Counter
# The penny counter you were promised

#Imports
import cv2 
import numpy as np

# Variables
valGauss=1
valKernel=7

# Still variables, but these are image remixes, you get the jist of 'em
original = cv2.imread('mrAbePennies.png')
grays = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(grays, (valGauss,valGauss), 0)
canny = cv2.Canny(gauss, 60, 100)
kernel = np.ones((valKernel, valKernel),np.uint8)
end = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

# We search for contours, we use "end" mind you, for that is the image remix that went thru all the preparation needed for the program to more easily understand the original image
contornos, jerarquía=cv2.findContours(end.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

# We count the borders, for each one we add one, this is not quite perfect as it may overcount borders (Be it because it counted the coin details or some other thing)
print("Coins found: {}".format(len(contornos)))

# We draw the contours in the original image
cv2.drawContours(original, contornos, -1, (255,0,255),2) # 255,0,255, my other signature color because it's one of the few RGB colors I can bother to remember, I'm more of a #F0F8FF gal y'know?

# Show other results if you'd like
#cv2.imshow("Grays",grays)
#cv2.imshow("Gauss",gauss)
#cv2.imshow("Canny",canny)
#cv2.imshow("Final Image",end) # Looks funny, indie game funny fufu. Anyways if there are any phantom borders check this one

cv2.imshow("Result", original) #We show the final result with drawn borders around coins
cv2.waitKey(0)