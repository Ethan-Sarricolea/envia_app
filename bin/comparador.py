import cv2
import numpy as np



class IMGcomaparator:
    def __init__(self) -> None:
        self.logos = [r'src\logos\DHL.jpg',
         r"src\logos\ESTAFETA.jpg"
         ,r"src\logos\FEDEX.jpg",
         r"src\logos\JYT.jpg",
         r"src\logos\PAQUETEXPRESS.jpg",
         r"src\logos\REDPACK.jpg",
         r'src\logos\UPS.jpg']
        self.nombres = ["DHL","Estafeta","FEDEX","J&T","PaqueteExpress","REDPACK","UPS"]
        
        
    def comparacion(self,image):
        # Comparacion de la imagen con los logos
        self.resultsList = []
        # src\screenshots\screenshot1.jpg
        self.original = cv2.imread(image)
        for logo in self.logos:
            self.image_to_compare = cv2.imread(logo)
            self.redimension()
        return self.comparacion_results()

    def redimension(self):
        # Restar las imágenes con redimensión
        self.image_to_compare_resized = cv2.resize(self.image_to_compare, (self.original.shape[1], self.original.shape[0]))
        self.difference = cv2.subtract(self.original, self.image_to_compare_resized)
        self.equalsImage()

    def equalsImage(self):
        #Identificar igualdad total
        b, g, r = cv2.split(self.difference)
        print(cv2.countNonZero(b))
        if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            self.resultsList.append(100)
        else: 
            self.similitud()


    def similitud(self):

        self.shift = cv2.xfeatures2d.SIFT_create()
        self.kp_1, self.desc_1 = self.shift.detectAndCompute(self.original, None)
        self.kp_2, self.desc_2 = self.shift.detectAndCompute(self.image_to_compare, None)
        """print("Keypoints 1st image", str(len(self.kp_1)))
        print("Keypoints 2st image", str(len(self.kp_2)))"""
        self.index_params = dict(algorithm=0, trees=5)
        self.search_params = dict()
        self.flann = cv2.FlannBasedMatcher(self.index_params,self.search_params)
        self.matches = self.flann.knnMatch(self.desc_1, self.desc_2, k=2)
        self.results()

    def results(self):
        # Deteccion de good matches y porcentaje de similitud, agregandolo a la lista
        self.good_points = []
        for m, n in self.matches:
            if m.distance < 0.6*n.distance:
                self.good_points.append(m)

        number_keypoints = 0
        if (len(self.kp_1) <= len(self.kp_2)):
            number_keypoints = len(self.kp_1)
        else:
            number_keypoints = len(self.kp_2)
        #print("GOOD matches",len(self.good_points))
        #print("Que tan bueno es el match", len(self.good_points) / number_keypoints * 100, "%")
        self.resultsList.append(len(self.good_points) / number_keypoints * 100)

    def comparacion_results(self):
        # Tomar el indice maximo de porcentaje y cambiarlo por nombre
        i = self.resultsList.index(max(self.resultsList))
        return self.nombres[i]

"""lala = IMGcomaparator()
print(lala.comparacion())"""