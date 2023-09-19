from PIL import Image
import os

class takeCropPhoto:
    def __init__(self):
        pass
    
    def takePhoto():
        #command = "raspistill -o image" + str(i) + ".jpg"
        command = "raspistill -o image.jpg"
        os.system(command)
        return

    def cropPhoto():
        img0 = Image.open("image.jpg")
        img_cropped = img0.crop((1250, 800, 1450, 900))
        img_cropped.save("img_cropped.jpg")
        return

