# Nitin Rai
# Department of Agriculture and Biosystems Engineering
# North Dakota State University
from PIL import Image
import os, sys
# This was my file path
path = "C:/Users/nitin/OneDrive/Desktop/Python_Algorithms/Dataset_Preparation/train/sugar_beet/"
dirs = os.listdir(path)
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((224,224), Image.ANTIALIAS)
            imResize.save(f + ' image_.png', 'png', quality=90) # Change it to .jpg, or any file type you want
resize()
