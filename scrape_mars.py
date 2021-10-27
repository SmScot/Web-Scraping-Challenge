#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[3]:


# Declare the database
db = client.mars_db
# Declare the collection
mars = db.mars


# In[4]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

# Request URL
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')


# In[5]:


soup


# In[6]:


# print article title
news_title = soup.find('div', class_= 'content_title').text
print(news_title)


# In[7]:


# print article preview
news_p = soup.find('div', class_= 'rollover_description_inner').text
print(news_p)


# In[8]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[10]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

results = soup.find('a', class_='showimg fancybox-thumbs')['href']


# In[11]:


featured_image_url = url + results
print(featured_image_url)


# In[12]:


url = 'https://galaxyfacts-mars.com/'


# In[13]:


# Use Panda's `read_html` to parse the url
tables = pd.read_html(url)
tables


# In[14]:


# Create dataframe
comparisons_df = tables[0]
comparisons_df.columns = ['Description', 'Mars', 'Earth']
comparisons_df.set_index('Description', inplace=True)
comparisons_df


# In[15]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[16]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere_image_urls = []

browser.links.find_by_partial_text('Cerberus').click()
soup = BeautifulSoup(browser.html, 'html.parser')


# In[17]:


results = soup.find_all("a")

for result in results:
    if result.text.strip() == "Original":
        image_url = result["href"]
        
title = soup.find("h2", class_="title").text

x = {"title": title,
    "image_url": image_url}
hemisphere_image_urls.append(x)
print(hemisphere_image_urls)


# In[18]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[19]:


browser.links.find_by_partial_text('Schiaparelli').click()

html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[20]:


results = soup.find_all("a")

for result in results:
    if result.text.strip() == "Original":
        image_url = result["href"]
        
title = soup.find("h2", class_="title").text

x = {"title": title,
    "image_url": image_url}
hemisphere_image_urls.append(x)
print(hemisphere_image_urls)


# In[21]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[22]:


browser.links.find_by_partial_text('Syrtis Major').click()

html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[23]:


results = soup.find_all("a")

for result in results:
    if result.text.strip() == "Original":
        image_url = result["href"]
        
title = soup.find("h2", class_="title").text

x = {"title": title,
    "image_url": image_url}
hemisphere_image_urls.append(x)
print(hemisphere_image_urls)


# In[24]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[25]:


browser.links.find_by_partial_text('Valles Marineris').click()

html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[26]:


results = soup.find_all("a")

for result in results:
    if result.text.strip() == "Original":
        image_url = result["href"]
        
title = soup.find("h2", class_="title").text

x = {"title": title,
    "image_url": image_url}
hemisphere_image_urls.append(x)
print(hemisphere_image_urls)


# In[27]:


browser.quit()





