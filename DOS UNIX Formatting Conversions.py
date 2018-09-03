
# coding: utf-8

# In[ ]:


#convert DOS-type txt files to UNIX-type txt files 

import sys, re, os
from os import listdir


def DOS_to_UNIX(filename_complete):
    f = open(filename_complete, "r")
    data = f.read() 
    f.close()
    newdata = data.replace("\r\n", "\n") 
    f2 = open(filename_complete, "w+")
    f2.write(newdata)
    f2.close()

def UNIX_to_DOS(filename_complete):
    f = open(filename_complete, "r")
    data = f.read()
    f.close()
    newdata = data.replace("\n", "\r\n") 
    f2 = open(filename_complete, "w+")
    f2.write(newdata)
    f2.close()

directory ="Desktop/Test" #Enter directory
files = listdir(directory)
print(files) #print list files that will be converted
for filename in files:
    DOS_to_UNIX(directory+"/"+filename)


    

