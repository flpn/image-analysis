import cv2


image_1 = cv2.imread('./images/3D-Matplotlib.png')
image_2 = cv2.imread('./images/mainlogo.png')

# add = image_1 + image_2
# add = cv2.add(image_1, image_2)

rows, cols, channels = image_2.shape
roi = image_1[0:rows, 0:cols]

image_to_gray = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(image_to_gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

image_1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
image_2_fg = cv2.bitwise_and(image_2, image_2, mask=mask)

dst = cv2.add(image_1_bg, image_2_fg)
image_1[0:rows, 0:cols] = dst

cv2.imshow('image', image_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
