# Nothing much so I'll explain the lines

import cv2 # We import cv2
image = cv2.imread('contour.jpg') # We store the image in the "image" variable
cv2.imshow('Image here, yeap',image) # Then we show said image in a window with a title
cv2.waitKey(0) # We wait for a key, any key
cv2.destroyAllWindows() # Once pressed it destroys the window/kils the program