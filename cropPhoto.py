from PIL import Image

img0 = Image.open("image14.jpg")
print(img0.size)

img_cropped = img0.crop((1750, 1200, 1890, 1290))
img_cropped.save("image14_cropped.jpg")
