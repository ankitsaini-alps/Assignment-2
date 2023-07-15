#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Install

get_ipython().system('pip install requests')

get_ipython().system('pip install BeautifulSoup')

get_ipython().system('pip install pandas as pd')


# In[1]:


# Importing Liabraries

import requests
from bs4 import BeautifulSoup
import pandas as pd


# "Getting the Name of Authors in 1 to 5 pages"

# In[13]:


BeautifulQuotes = []

# Using loop to iterate 

for i in range(1, 6):
    url = f"http://quotes.toscrape.com/page/{i}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all("div", class_="quote")

    for element in elements:
        name = element.find("small", class_="author").text
        quote = element.find("span", class_='text').text
        tags = element.find("meta", class_="keywords")["content"].split(",")
        BeautifulQuotes.append({"Name": name, "Quote": quote, "Tags": tags})


# In[5]:


df = pd.DataFrame(BeautifulQuotes,columns = ['Name','Quotes','Tags'])
df


# In[17]:


df.to_csv("BeautifulQuotes.csv")


# In[ ]:




