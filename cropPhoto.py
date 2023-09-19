from PIL import Image

img0 = Image.open("test1.jpg")
print(img0.size)

img_cropped = img0.crop((1250, 800, 1450, 900))
img_cropped.save("test1_cropped.jpg")
