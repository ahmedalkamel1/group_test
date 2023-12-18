from PIL import Image

import numpy as np

img=Image.open("teaser.jpg")#فتح الصورة

print(img.size,img.width,img.height,img.format,img.mode)# طباعة معلومات عن الصورة

img.show()# عرض الصورة

imgarry=np.array(img)# تحويل الصورة كمصفوفة 
print(img)# طباعة الصورة المحولة 

x=(0,100,300,190)# أبعاد الصورة

crop_img=img.crop(x)# قص الصورة
crop_img.show()
crop_img.save("crop.jpg")# حفظ الصورة 


