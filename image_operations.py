import cv2


image = cv2.imread('./images/watch.jpg', cv2.IMREAD_COLOR)

pixel = image[55, 55]
image[55, 55] = [255, 255, 255]
print(pixel)

pixels = image[100:150, 100:150]

print(image.shape)
print(image.size)
print(image.dtype)

watch_face = image[37:111, 107:194]
image[0:74, 0:87] = watch_face

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
