import cv2 as cv
import sys
 
img = cv.imread("data/starry_night.jpg")
 
if img is None:
    sys.exit("No se puede leer la imagen.")
 
cv.imshow("Imagen", img)
k = cv.waitKey(0)
 
if cv.waitKey(0) == ord('q'):
    img.release()
    cv.destroyAllWindows()