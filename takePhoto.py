from PIL import Image
import os
import time

TIMEBETWEEN = 5

imax = 1000
i = 0

while True and i < imax:
    os.system("raspistill -o image%d.jpg", i)
    time.sleep(TIMEBETWEEN)
    i += 1
    
for i in range(0,imax):
    img0 = Image.open("test%d.jpg", i)
    img_cropped = img0.crop((1250, 800, 1450, 900))
    img_cropped.save("test%d_cropped.jpg", i)