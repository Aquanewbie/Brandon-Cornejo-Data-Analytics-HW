import pandas as pd
import lxml
import xml
from bs4 import BeautifulSoup
import requests
from splinter import Browser
    
# executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
# browser = Browser('chrome', **executable_path, headless=False)   

# url='https://mars.nasa.gov/news/'
# browser.visit(url)

# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')
 
# Title =soup.find('div', class_='content_title').text
# print(Title)
    
# Paragraph = soup.find('div', class_='article_teaser_body').text
# print(Paragraph)

# executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
# browser = Browser('chrome', **executable_path, headless=False)
# url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# browser.visit(url)
# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')

# Img = soup.find('a', class_='button fancybox')
# ImgPath= (Img['data-fancybox-href'])
# featured_image_url = (f'https://www.jpl.nasa.gov{ImgPath}')
# featured_image_url
# print (featured_image_url)

# url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# browser.visit(url)
# browser.click_link_by_partial_text('FULL IMAGE')
# html = browser.html
# Img = soup.find('a', class_='button fancybox')
# ImgPath= (Img['data-fancybox-href'])
# featured_image_url = (f'https://www.jpl.nasa.gov{ImgPath}')
# featured_image_url
# print (featured_image_url)

executable_path = {'executable_path':"chromedriver"}
browser = Browser('chrome', **executable_path, headless=True)

url='https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
Title = soup.find('div', class_='content_title').get_text()
Paragraph = soup.find('div', class_='article_teaser_body').get_text()

print(Title + Paragraph)