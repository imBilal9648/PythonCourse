import cv2

im = cv2.imread('multimedia\sample_small.jpeg')
print(im.shape)
cv2.imshow('Image window', im)
cv2.waitKey(0)