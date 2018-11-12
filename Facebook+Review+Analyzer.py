
# coding: utf-8

# In[83]:


import ast
from bs4 import BeautifulSoup

#still need to do url to html bit to completely simplify process, then follow up with word density analysis.

with open("Desktop/Pisticci2.htm") as fp:
    soup=BeautifulSoup(fp)
    
reviews = soup.find_all("div", {"data-ad-preview": "message"})
i=1;
for re in reviews:
    print(str(i)+":"+re.text)
    i+=1



# In[ ]:




