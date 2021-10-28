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

def scrape_info():

# In[2]:


    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

# Request URL
    response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')


# In[3]:


    soup


# In[4]:


# print article title
    news_title = soup.find('div', class_= 'content_title').text
    print(news_title)


# In[5]:


# print article preview
    news_p = soup.find('div', class_= 'rollover_description_inner').text
    print(news_p)


# In[6]:


# Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


# In[7]:


    url = 'https://spaceimages-mars.com/'
    browser.visit(url)


# In[8]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('a', class_='showimg fancybox-thumbs')['href']


# In[9]:


    featured_image_url = url + results
    print(featured_image_url)


# In[10]:


    url = 'https://galaxyfacts-mars.com/'


# In[11]:


# Use Panda's `read_html` to parse the url
    tables = pd.read_html(url)
    tables


# In[12]:


# Create dataframe
    comparisons_df = tables[0]
    comparisons_df.columns = ['Description', 'Mars', 'Earth']
    comparisons_df.set_index('Description', inplace=True)
    comparisons_df


    # In[13]:


    mars_facts = comparisons_df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
    print(mars_facts)


    # In[14]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # In[15]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere_image_urls = []

    browser.links.find_by_partial_text('Cerberus').click()
    soup = BeautifulSoup(browser.html, 'html.parser')


    # In[16]:


    results = soup.find_all("a")

    for result in results:
        if result.text.strip() == "Sample":
            image_url = result["href"]
            
    title = soup.find("h2", class_="title").text

    x = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(x)
    print(hemisphere_image_urls)


    # In[17]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # In[18]:


    browser.links.find_by_partial_text('Schiaparelli').click()

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[19]:


    results = soup.find_all("a")

    for result in results:
        if result.text.strip() == "Sample":
            image_url = result["href"]
            
    title = soup.find("h2", class_="title").text

    x = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(x)
    print(hemisphere_image_urls)


    # In[20]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # In[21]:


    browser.links.find_by_partial_text('Syrtis Major').click()

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[22]:


    results = soup.find_all("a")

    for result in results:
        if result.text.strip() == "Sample":
            image_url = result["href"]
            
    title = soup.find("h2", class_="title").text

    x = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(x)
    print(hemisphere_image_urls)


    # In[23]:


    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # In[24]:


    browser.links.find_by_partial_text('Valles Marineris').click()

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[25]:


    results = soup.find_all("a")

    for result in results:
        if result.text.strip() == "Sample":
            image_url = result["href"]
            
    title = soup.find("h2", class_="title").text

    x = {"title": title,
        "image_url": image_url}
    hemisphere_image_urls.append(x)
    print(hemisphere_image_urls)


    # In[26]:


    browser.quit()

    scraped_data = {
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_image_url" : featured_image_url,
        "mars_facts" : mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    return scraped_data

if __name__ == "__main__":
    scrape_info()