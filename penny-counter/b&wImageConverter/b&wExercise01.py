# We convert an image to black and white

import cv2 # We import cv2
image = cv2.imread('contour.jpg') # We store the image in the "image" variable
grays = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # We gray out the image, store it in grays, which is just the image but gray

cv2.imshow('OG Image', image)
cv2.imshow('Gray Image', grays)
cv2.waitKey(0) # We wait for a key, any key
cv2.destroyAllWindows() # Once pressed it destroys the window/kills the program