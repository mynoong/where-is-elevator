from PIL import Image
import os
import time

TIMEBETWEEN = 5

while True:
    os.system("raspistill -o image.jpg")
    time.sleep(TIMEBETWEEN)
    
