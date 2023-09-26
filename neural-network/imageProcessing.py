# Packages/libraries with processing images through opencv-python library

import cv2
import numpy as np
import matplotlib.pyplot as plt

class imageProcessing:
    def __init__():
        pass
    
    def RGBtoGRAY(img):  #Make an image of RGB into gray
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img_gray = hsv[:, :, 2]
        return img_gray
    
    def gaussianBlur(img, ksize): 
    #Blur an image and minimize noises
    #ex) ksize = (3, 3)
        img_blurred = cv2.GaussianBlur(img, ksize = ksize, sigmaX = 0)
        return img_blurred
    
    def adaptiveThresholdGaussian(img, blockSize, C):
    #Threshold pixel figures by 0 or 255 using adaptive gaussian threshold
    #ex) blockSize = 35, C = -3
        img_thresholded = cv2.adaptiveThreshold(
            img,
            maxValue = 255.0,
            adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresholdType = cv2.THRESH_BINARY,
            blockSize = blockSize,
            C = C
        )
        return img_thresholded
    
    def otsuBinaryThreshold(img):
        _, img_thresholded = cv2.threshold(
            img,
            thresh = 0,
            maxval = 255.0,
            type = cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return img_thresholded
    
    def drawContours(img): #Draw contours of an image
        height, width = img.shape
        img_contoured = np.zeros((height, width), dtype = np.uint8)
        
        contours, _ = cv2.findContours(
            img,
            mode = cv2.RETR_LIST,
            method = cv2.CHAIN_APPROX_SIMPLE
        )
        cv2.drawContours(
            img_contoured,
            contours = contours,
            contourIdx = -1,
            color = (255, 255, 255)
        )
        return img_contoured, contours
    
    def drawBoundaryBoxes(img, contours): 
    #Generate boundary boxes of elements in an image
        height, width = img.shape
        img_bbox = np.zeros((height, width), dtype = np.uint8)
        
        contours_dict = []

        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(
                img_bbox,
                pt1 = (x, y),
                pt2 = (x + w, y + h),
                color = (255, 255, 255),
                thickness = 2
            )
            contours_dict.append({
                'contour': c, 'x': x, 'y': y, 'w': w, 'h': h, 
                'cx': x + (w / 2), 'cy': y + (h / 2)
            })
        
        return img_bbox, contours_dict
    
    def selectBboxes(img, contours_dict): 
    #Select candidates of boundary boxes by digit size
        height, width = img.shape
        
        MIN_AREA = 40
        MIN_WIDTH, MIN_HEIGHT = 10, 30
        MAX_WIDTH, MAX_HEIGHT = 50, 80
        MIN_RATIO, MAX_RATIO = 0.10, 0.9

        img_candi_bbox = np.zeros((height, width), dtype=np.uint8)
        contours_candi_dict = []
        cnt = 0
        
        for c in contours_dict:
            area = c['w'] * c['h']
            ratio = c['w'] / c['h']
    
            if area > MIN_AREA and \
                MIN_WIDTH < c['w'] < MAX_WIDTH and \
                MIN_HEIGHT < c['h'] < MAX_HEIGHT and \
                MIN_RATIO < ratio < MAX_RATIO:
                    #c['idx'] = cnt
                    #cnt += 1
                    contours_candi_dict.append(c)
        
        for c in contours_candi_dict:
            cv2.rectangle(
                img_candi_bbox, 
                pt1 = (c['x'], c['y']), 
                pt2 = (c['x'] + c['w'], c['y'] + c['h']), 
                color = (255, 255, 255), thickness = 2
            )
        
        return img_candi_bbox, contours_candi_dict

    def getDigitImage(img, contours_candi_dict):
    # get image of each digit from dictionary "contours_candi_dict"
    # and store it in dictionary "img_digits"
        img_digits = []

        for c in contours_candi_dict:
            digit_height = c['h']
            digit_width = c['w']
            digit_cx = c['cx']
            digit_cy = c['cy']  
    
            img_digit = cv2.getRectSubPix(
                img, 
                patchSize = ( int(digit_width), int(digit_height) ),
                center = ( int(digit_cx), int(digit_cy) )
            )
            img_digits.append(img_digit)
        
        return img_digits
    
    def makeBorder(img):
        img_bordered = cv2.copyMakeBorder(
            img, 
            top = 20, bottom = 20, left = 20, right = 20, 
            borderType = cv2.BORDER_CONSTANT, value = (0, 0, 0)
        )
        return img_bordered  
    
    def checkPhoto(img, imageName):
    # save the processed image with a given imageName
    # ex) imageName = 'img_digit.jpg'
        plt.figure(figsize = (12, 10))
        plt.imshow(img, cmap = 'gray')
        plt.savefig(imageName)
         
    