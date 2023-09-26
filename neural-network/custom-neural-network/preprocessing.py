import cv2
from imageProcessing import imageProcessing as ip

for i in range(0, 250):
    pathAndName = "data/num_elevator_cropped/image" + str(i) + ".jpg"
    img = cv2.imread(pathAndName)
    img_gray = ip.RGBtoGRAY(img)
    img_blurred = ip.gaussianBlur(img_gray, (3,3))
    img_thresholded = ip.otsuBinaryThreshold(img_blurred)
    
    cv2.imwrite(pathAndName, img_thresholded)