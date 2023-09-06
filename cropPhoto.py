from PIL import Image

img0 = Image.open("test1.jpg")
print(img0.size)

img_cropped = img0.crop((1250, 700, 1450, 1000))
img_cropped.save("test1_cropped.jpg")
