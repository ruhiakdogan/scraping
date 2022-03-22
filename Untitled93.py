#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

html = requests.get("https://www.nesine.com/sportoto").text
soup = BeautifulSoup(html, "lxml")
matches = soup.find("tbody")
matchess = matches.find_all("tr")
list= []

for match in matchess:
    mac_name = match.find("span", class_="event-name").text.replace(" ","")
    oynanma = match.find("td", class_="select").text.replace(" ","")
    a = re.sub(r'\n', '', oynanma)
    b = a.split("%")
    d = (" ".join(b[1:2]))  
    e = (" ".join(b[2:3])) 
    f = (" ".join(b[3:4])) 
    list.append((mac_name.strip(),d,e,f))
              
k = pd.DataFrame(list,columns=["Match","1","X","2"])
print(k)


# In[ ]:




