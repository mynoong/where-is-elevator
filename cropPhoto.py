# Crop the images taken by raspberry pi into desired image size
# Elevator number images are 90 (height) * 120 (width)
from PIL import Image

for i in range(0, 250):
    name = "data/num_elevator/image" + str(i) + ".jpg"
    img0 = Image.open(name)
    
    name = "data/num_elevator_cropped/image" + str(i) + ".jpg"
    img_cropped = img0.crop((1750, 1200, 1870, 1290))
    img_cropped.save(name)

"""
print(img0.size)

img_cropped = img0.crop((1750, 1200, 1870, 1290))
img_cropped.save("image43_cropped.jpg")
"""