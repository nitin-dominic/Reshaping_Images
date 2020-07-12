#!/usr/bin/env python
# coding: utf-8

# In[54]:


from PIL import Image
import os, sys
path = "C:/Users/nitin/OneDrive/Desktop/Python_Algorithms/Dataset_Preparation/train/sugar_beet/"
dirs = os.listdir(path)


# In[55]:


def resize():

    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((224,224), Image.ANTIALIAS)
            imResize.save(f + ' image_.png', 'png', quality=150) # Change it to .jpg, or any file type you want

resize()

