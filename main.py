import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img0 = cv2.imread('test1_cropped.jpg')

height, width, channel = img0.shape

#Make an image of RGB into gray
hsv = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
img_gray = hsv[:, :, 2]

#Blur an image and minimize noises
img_blurred = cv2.GaussianBlur(img_gray, ksize = (7, 7), sigmaX = 0)

#Threshold pixel figures by 0 or 255 using adaptive gaussian threshold
img_thresholded = cv2.adaptiveThreshold(
    img_blurred,
    maxValue = 255.0,
    adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType = cv2.THRESH_BINARY,
    blockSize = 19,
    C = 9
)

#Draw contours of an image
img_contoured = np.zeros((height, width, channel), dtype = np.uint8)
contours, _ = cv2.findContours(
    img_thresholded,
    mode = cv2.RETR_LIST,
    method = cv2.CHAIN_APPROX_SIMPLE
)
cv2.drawContours(
    img_contoured,
    contours = contours,
    contourIdx = -1,
    color = (255, 255, 255)
)

#Generate boundary boxes of elements in an image
img_bbox = np.zeros((height, width, channel), dtype = np.uint8)
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
    contours_dict.append({'contour': c, 'x': x, 'y': y, 'w': w, 'h': h, 
                          'cx': x + (w / 2), 'cy': y + (h / 2)
    })

#Select candidates of boundary boxes by digit size
MIN_AREA = 40
MIN_WIDTH, MIN_HEIGHT = 10, 30
MAX_WIDTH, MAX_HEIGHT = 50, 80
MIN_RATIO, MAX_RATIO = 0.10, 0.9

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

img_candi_bbox = np.zeros((height, width, channel), dtype=np.uint8)
for c in contours_candi_dict:
    cv2.rectangle(img_candi_bbox, 
        pt1 = (c['x'], c['y']), 
        pt2 = (c['x'] + c['w'], c['y'] + c['h']), 
        color = (255, 255, 255), thickness = 2
    )

#Get infos of selected digits and find the matching number w/ pytesseract
img_digits = []
for c in contours_candi_dict:
    digit_height = c['h']
    digit_width = c['w']
    digit_cx = c['cx']
    digit_cy = c['cy']
    
    img_digit = cv2.getRectSubPix(
        img0, 
        patchSize = (int(digit_width), int(digit_height)),
        center = (int(digit_cx), int(digit_cy))
    )
    img_digits.append(img_digit)

for img_digit in img_digits:
    img_digit = cv2.GaussianBlur(
        img_digit, 
        ksize = (3, 3), 
        sigmaX = 0
    )
    img_digit = cv2.adaptiveThreshold(
        img_digit,
        maxValue = 255.0,
        adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType = cv2.THRESH_BINARY,
        blockSize = 19,
        C = 9
    )
    img_digit = cv2.copyMakeBorder(
        img_digit, 
        top = 20, bottom = 20, left = 20, right = 20, 
        borderType = cv2.BORDER_CONSTANT, value = (0, 0, 0)
    )
    
    chars = pytesseract.image_to_string(
        img_digit, lang = 'eng', config = '--psm 7'
        #let pytesseract know digits are alligned in a line
        #and use legacy engine to just perceive each digit, 
        #not to understand/interpret an image 
    )
    plt.figure(figsize = (12, 10))
    plt.imshow(img_digit, cmap = 'gray')
    plt.savefig('i.jpg')
    
    print(chars)
