
# coding: utf-8

# In[ ]:


#Generate train.txt file for darknet yolov3 model training from directory of annotation files

from os import listdir

files = listdir("Desktop/Annot") #folder containing .txt annotation files
path_from_root = "data/final/HH/Images/" #path of folder containing images
image_type = "jpg" 

#Change above fields as required

f = open("train.txt", "w+")
for file in files:
        ending = file[:-3]
        f.write(path_from_root+ending+image_type+"\n") 
        

