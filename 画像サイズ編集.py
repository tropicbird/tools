from PIL import Image
im=Image.open("./source/P3070541crop.jpg")
im.show()
size = im.size
shorter_length=min(size)
print(shorter_length)
im_crop = im.crop((0, 0, shorter_length, shorter_length))
im_resized=im_crop.resize((512,512))
im_resized.show()
im_resized.save("./source/cropped_resized.jpg", quality=95)