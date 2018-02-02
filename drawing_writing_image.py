import cv2
import numpy as np

image = cv2.imread('./images/watch.jpg', cv2.IMREAD_COLOR)

cv2.line(image, (0, 0), (150, 150), (255, 255, 255), 5)
cv2.rectangle(image, (15, 25), (50, 60), (255, 0, 0), 5)
cv2.circle(image, (100, 100), 15, (0, 255, 0), -1)

# draw a polygon
points = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(image, [points], True, (0, 0, 255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Hello world!', (110, 130), font, 1, (200, 255, 120), 5)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
