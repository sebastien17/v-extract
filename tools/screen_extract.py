import numpy
import cv2
from PIL import ImageGrab

def opencv_screenshot():
    # fullscreen
    pil_image = ImageGrab.grab().convert('RGB') 
    open_cv_image = numpy.array(pil_image) 
    # Convert RGB to BGR 
    return  open_cv_image[:, :, ::-1].copy() 

if(__name__ == "__main__"):
    cv2.imshow("screenshot", opencv_screenshot())
    cv2.waitKey(0)
    cv2.destroyAllWindows()