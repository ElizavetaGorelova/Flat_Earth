#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re


# In[2]:


r = urllib.request.urlopen('https://www.theflatearthsociety.org/forum/index.php?board=20.0').read()
soup = BeautifulSoup(r, 'lxml')
type(soup)


# In[3]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[4]:


print(soup.get_text())


# In[5]:


print(soup.prettify()[0:1000])


# In[6]:


for link in soup.find_all('a', attrs={'href': re.compile("^http")}):
    print(link)
type(link)


# In[7]:


file = open('parsed_data.txt', 'w')
for link in soup.find_all('a', attrs={'href': re.compile('^http')}):
    soup_link = str(link)
    print(soup_link)
    file.write(soup_link)
file.flush()
file.close

