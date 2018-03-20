import cv2
import imutils

image = cv2.imread('image.jpg')
image = imutils.rotate(image, 270)
cv2.imwrite('image.jpg', image)
print("Rotation complete.")
# change this as you see fit
