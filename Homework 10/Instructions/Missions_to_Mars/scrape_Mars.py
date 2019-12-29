import pandas as pd
import lxml
import xml
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import datetime as dt

def internetscrape():
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    
    #* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) 
    # and collect the latest News Title and Paragraph Text. 
    # Assign the text to variables that you can reference later.
    url='https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Title = soup.find('div', class_='content_title').get_text()
    Paragraph = soup.find('div', class_='article_teaser_body').get_text()

    #* Visit the url for JPL Featured Space Image [here]
    #(https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    #* Use splinter to navigate the site and find the image url for the current Featured Mars 
    #Image and assign the url string to a variable called `featured_image_url`.
    #* Make sure to find the image url to the full size `.jpg` image.
    #* Make sure to save a complete url string for this image.
      
    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    Img = soup.find('a', class_='button fancybox')
    ImgPath= (Img['data-fancybox-href'])
    featured_image_url = (f'https://www.jpl.nasa.gov{ImgPath}')


    #* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) 
    #and scrape the latest Mars weather tweet from the page. Save the tweet text for the 
    # weather report as a variable called `mars_weather`.

    url='https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Find Latest Weather Tweet
    LatestWeatherTweet=soup.find("div", {"data-reply-to-users-json":"""[{"id_str":"786939553","screen_name":"MarsWxReport","name":"Mars Weather","emojified_name":{"text":"Mars Weather","emojified_text_as_html":"Mars Weather"}}]"""})
    mars_weather=LatestWeatherTweet.p.text

    ### Mars Facts
    #* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table 
    #containing facts about the planet including Diameter, Mass, etc.

    #* Use Pandas to convert the data to a HTML table string.
    url='https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    MarsDataList1=[]
    MarsDataList2=[]
    MarsData=soup.find('tbody')
    for i in MarsData:
        MarsDataList1.append(i.find('td', class_="column-1").get_text())
        MarsDataList2.append(i.find('td', class_="column-2").get_text())
    #Create Pandas Dataframe
    df = pd.DataFrame(MarsDataList2,  MarsDataList1)
    #Set to Dataframe to HTML
    MarsDataHTML = (df.to_html(classes="table table-striped"))


    ### Mars Hemispheres
    #* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
    #to obtain high resolution images for each of Mar's hemispheres.
    #* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    #* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
    #* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    #```python
    # Example:
    #hemisphere_image_urls = [
    #    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    #    {"title": "Cerberus Hemisphere", "img_url": "..."},
    #    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    #   {"title": "Syrtis Major Hemisphere", "img_url": "..."},

    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    MarsHemispheres=soup.find_all('h3')
    MarsHemisphereslist=[]
    for Hemisphere in MarsHemispheres:
        MarsHemisphereslist.append(Hemisphere.text)
    Hemisphere1=MarsHemisphereslist[0]
    Hemisphere2=MarsHemisphereslist[1]
    Hemisphere3=MarsHemisphereslist[2]
    Hemisphere4=MarsHemisphereslist[3]
    MarsHemisphereList=[Hemisphere1, Hemisphere2, Hemisphere3, Hemisphere4]

    MarsHemisphereListUrls=[]
    for x in MarsHemisphereList:
        browser.visit(url)
        browser.click_link_by_partial_text(x)
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')
        Img = soup.find('img', class_="wide-image")
        ImagePath = Img['src']
        MarsHemisphereListUrls.append(f'https://astrogeology.usgs.gov/{ImagePath}')

    Hemisphere1Url=MarsHemisphereListUrls[0]
    Hemisphere2Url=MarsHemisphereListUrls[1]
    Hemisphere3Url=MarsHemisphereListUrls[2]
    Hemisphere4Url=MarsHemisphereListUrls[3]

    hemisphere_image_urls = [{"Title": Hemisphere1, "Url": Hemisphere1Url}, 
                            {"Title": Hemisphere2, "Url": Hemisphere2Url},
                            {"Title": Hemisphere3, "Url": Hemisphere3Url},
                            {"Title": Hemisphere4, "Url": Hemisphere4Url}]

    infoscraped = {
        "NewsTitle": Title,
        "NewsParagraph": Paragraph,
        "ImageandUrl": featured_image_url,
        "HemisphereURLDict": hemisphere_image_urls,
        "WeatherTweet": mars_weather,
        "MarsDataHTML": MarsDataHTML,
        "last_modified": dt.datetime.now()
    }

    browser.quit()
    return infoscraped
    
if __name__ == "__main__":
    print('Yup')
