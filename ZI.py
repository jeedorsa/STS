import cv2
import numpy as np

W = 400	
img = cv2.imread("imagen_grua.jpg")
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Over the Clouds - gray", gray_image)
line_type = 8
inicio = [0, 0]
inicio_Z2 = [1100,0]
# Create some points
pos_Z1 = np.array([inicio, 
			      [inicio[0] + 1035, inicio[1]],
			      [inicio[0] + 1035, inicio[1] + 320],
			      [inicio[0] + 750 , inicio[1] + 1080], 
			      [inicio[0], inicio[1] + 1080]], 
			      np.int32)

pos_Z2 = np.array([inicio_Z2, 
                  [inicio_Z2[0] + 920, inicio_Z2[1]],
                  [inicio_Z2[0] + 920, inicio_Z2[1] + 1080],
                  [inicio_Z2[0] + 290, inicio_Z2[1] + 1080], 
                  [inicio_Z2[0], inicio_Z2[1] + 310]], 
                  np.int32) 


cv2.fillPoly(img, [pos_Z1], (0, 0, 0), line_type)
cv2.fillPoly(img, [pos_Z2], (0, 0, 0), line_type)
cv2.imshow("Over the Clouds", img)
cv2.imwrite("prueba.jpg", img)
if cv2.waitKey(0) == (ord('q') or ord('Q')):
	cv2.destroyAllWindows()
cv2.destroyAllWindows()