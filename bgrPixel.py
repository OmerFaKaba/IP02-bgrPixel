import cv2
import numpy as np

wolfImage = cv2.imread("wolf.png")

cv2.imshow("wolf image",wolfImage)


print(wolfImage[(230,80)]) # Prints the pixel value at position (230, 80)


print("Size of image " + str(wolfImage.size))  # Prints the total number of elements (pixels) in the image
print("Features of the image " + str(wolfImage.shape)) # Prints the dimensions (height, width, channels) of the image
print("Type of image " + str(wolfImage.dtype)) # Prints the data type of the image's elements (e.g., uint8, float32)

wolfImage[50,30] = [255,255,255]

for i in range(wolfImage.shape[2]):
    wolfImage[70,i] = [255,255,255]


cv2.imshow("wolf image",wolfImage)

cv2.waitKey(0)
cv2.destroyAllWindows()