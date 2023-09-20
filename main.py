import time
import cv2
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
from takeCropPhoto import takeCropPhoto as tcp
from imageProcessing import imageProcessing as ip

while True:
    tcp.takePhoto
    tcp.cropPhoto
    
    img0 = cv2.imread('image_cropped.jpg')
    height, width, channel = img0.shape

    #Make an image of RGB into gray
    img_gray = ip.RGBtoGRAY(img0)
    ip.checkPhoto(img_gray, 'image_gray.jpg')


    #Blur an image and minimize noises
    ksize = (3, 3)
    img_blurred = ip.gaussianBlur(img_gray, ksize)
    ip.checkPhoto(img_blurred, 'image_blurred.jpg')


    #Threshold pixel figures by 0 or 255 using adaptive gaussian threshold
    blockSize = 45
    C = -3
    img_thresholded = ip.adaptiveThresholdGaussian(img_blurred, blockSize, C)
    ip.checkPhoto(img_thresholded, 'image_thresholded.jpg')


    #Draw contours of an image
    img_contoured, contours = ip.drawContours(img_thresholded)
    ip.checkPhoto(img_contoured, 'image_contoured.jpg')


    #Generate boundary boxes of elements in an image
    img_bbox, contours_dict = ip.drawBoundaryBoxes(img_contoured, contours)
    ip.checkPhoto(img_bbox, 'image_bbox.jpg')


    #Select candidates of boundary boxes by digit size
    img_candi_bbox, contours_candi_dict = ip.selectBboxes(img_bbox, contours_dict)
    ip.checkPhoto(img_candi_bbox, 'image_candi_bbox.jpg')


    #Get image of each digit from dictionary "contours_candi_dict"
    #and store it in dictionary "img_digits"
    img_digits = ip.getDigitImage(img_gray, contours_candi_dict)


    #Get infos of selected digits and find the matching number w/ pytesseract
    chars = ""

    for img_digit in img_digits:
        ksize = (3, 3)
        img_digit = ip.gaussianBlur(img_digit, ksize)
        blockSize = 45
        C = -3
        img_digit = ip.adaptiveThresholdGaussian(img_digit, blockSize, C)
        #img_digit = ip.otsuBinaryThreshold(img_digit)
        img_digit = ip.makeBorder(img_digit)
    
        _, img_digit = cv2.threshold(
            img_digit,
            thresh = 0,
            maxval = 255.0,
            type = cv2.THRESH_BINARY_INV
        )
    
        ip.checkPhoto(img_digit, 'image_digit.jpg')

        char = pytesseract.image_to_string(
            img_digit, lang = 'eng', 
            config = '--psm 10 -c tessedit_char_whitelist=0123456789'
            #config = '--psm 7 --oem 0 -c tessedit_char_whitelist=0123456789'
            #let pytesseract know it is a single digit
            #and use legacy engine to just perceive each digit, 
            #not to understand/interpret an image 
        )
        char = char[0]
        chars += char
    
    print(chars)

    TIMEBETWEEN = 3
    time.sleep(TIMEBETWEEN)
