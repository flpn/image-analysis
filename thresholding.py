import cv2


image = cv2.imread('./images/bookpage.jpg', cv2.IMREAD_COLOR)

ret, threshold = cv2.threshold(image, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret_2, grayscaled_threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaussian = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', image)
cv2.imshow('threshold', threshold)
cv2.imshow('grayscaled threshold', grayscaled_threshold)
cv2.imshow('gaussian', gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
