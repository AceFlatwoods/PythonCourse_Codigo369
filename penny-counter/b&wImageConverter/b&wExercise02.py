# We show the contours of the images, the borders and such

import cv2 # We import cv2
image = cv2.imread('contour.jpg') # We store the image in the "image" variable
grays = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # We gray out the image, store it in grays, which is just the image but gray
_,treshold = cv2.threshold(grays, 100, 255, cv2.THRESH_BINARY) #Treshold for the image src, thresh, maxval, type. Min and max threshold is  100 and 255. Used for the contour
contour, order = cv2.findContours(treshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # We find the borders
cv2.drawContours(image, contour, -1, (255,63,52), 3) # We draw the borders


cv2.imshow('OG Image', image)
cv2.waitKey(0) # We wait for a key, any key
cv2.destroyAllWindows() # Once pressed it destroys the window/kills the program