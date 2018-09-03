
# coding: utf-8

# In[ ]:


#convert darknet yolov3 xml annotations to txt format

import xml.etree.ElementTree as ET


def create_txt(filename_sent):
    filename = "Downloads\scuta_train_annots_clean" "\\"+ filename_sent
    print(filename)
    data = ET.parse(filename)
    root = data.getroot()
    filewidth = int(root.find('size/width').text)
    fileheight = int(root.find('size/height').text)

    filetowrite = filename[:len(filename)-4]+".txt"
    file = open(filetowrite,'w') 

 

    for object in root.iter('object'):
        xmin= int(object.find('./bndbox/xmin').text)
        ymin= int(object.find('./bndbox/ymin').text)
        xmax= int(object.find('./bndbox/xmax').text)
        ymax= int(object.find('./bndbox/ymax').text)
        xcords = ((xmax+xmin)/2)/filewidth
        ycords = ((ymax+ymin)/2)/fileheight
        height = (ymax - ymin)/fileheight
        width = (xmax - xmin)/filewidth
        file.write("0"+" "+str(round(xcords,6))+" "+str(round(ycords,6))+ " "+str(round(width,6))+" "+str(round(height,6))+'\n')
    
    file.close() 
    
from os import listdir
from os.path import isfile, join
mypath = "\Downloads\scuta_train_annots_clean"
onlyfiles = listdir('Downloads\scuta_train_annots_clean')
for each in onlyfiles:
    create_txt(each)


# In[ ]:


from os import listdir
from os.path import isfile, join
mypath = "\Downloads\scuta_train_annots_clean"
onlyfiles = listdir('Downloads\scuta_train_annots_clean')
for each in onlyfiles:
    print("data\\scuta_train_annots_clean\\"+each[:len(each)-3]+"jpg")
    
    

