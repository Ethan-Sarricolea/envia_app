import cv2
import numpy as np

logos = [r'src\logos\DHL.jpg',
         r"src\logos\ESTAFETA.jpg"
         ,r"src\logos\FEDEX.jpg",
         r"src\logos\JYT.jpg",
         r"src\logos\PAQUETEXPRESS.jpg",
         r"src\logos\REDPACK.jpg",
         r'src\logos\UPS.jpg']


original = cv2.imread("src\screenshots\prueba.jpg")# src\screenshots\screenshot1.jpg
image_to_compare = cv2.imread(logos[1])

# Redimensionar la segunda imagen para que coincida con el tamaño de la primera imagen
image_to_compare_resized = cv2.resize(image_to_compare, (original.shape[1], original.shape[0]))

# Restar las imágenes
difference = cv2.subtract(original, image_to_compare_resized)

# 1) Check if 2 images are equals

difference = cv2.subtract(original, image_to_compare_resized)
b, g, r = cv2.split(difference)
print(cv2.countNonZero(b))
if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
    print('Las imagenes son completamente iguales')
else: 
    print('Las imagenes no son iguales')

# 2) Check la similitud de las dos imagenes
shift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = shift.detectAndCompute(original, None)
kp_2, desc_2 = shift.detectAndCompute(image_to_compare, None)

print("Keypoints 1st image", str(len(kp_1)))
print("Keypoints 2st image", str(len(kp_2)))

index_params = dict(algorithm=0, trees=5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc_1, desc_2, k=2)

good_points = []
for m, n in matches:
    if m.distance < 0.6*n.distance:
        good_points.append(m)

number_keypoints = 0
if (len(kp_1) <= len(kp_2)):
    number_keypoints = len(kp_1)
else:
    number_keypoints = len(kp_2)

print("GOOD matches",len(good_points))
print("Que tan bueno es el match", len(good_points) / number_keypoints * 100, "%")

result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
cv2.imshow("Result", cv2.resize(result, None, fx = 0.4, fy=0.4))
cv2.imwrite("Feature_matching.jpg", result)

#cv2.imshow("Original", original)
#cv2.imshow("Duplicate", image_to_compare)
cv2.waitKey(0)
cv2.destroyAllWindows()