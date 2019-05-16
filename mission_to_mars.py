# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests


def scrape_all():

        # URL of page to be scraped
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)


        # Retrieve page with the requests module
        #response = requests.get(url)
        browser.visit(url)


        # Create BeautifulSoup object; parse with 'html.parser'
        soup = BeautifulSoup(browser.html, 'html.parser')


        # Examine the results, then determine element that contains sought info
        #print(soup)


        title = soup.title.text
        print(title)


        results = soup.find_all('li', class_='slide')


        #print(results)


        # Loop through returned results
        for result in results:
                # Identify and return title of listing
                news_title= result.find('div', class_='content_title').text
                news_p= result.find('div', class_='rollover_description_inner').text



        #print(news_title)


        news_title=  results[0].find('div', class_='content_title').text


        #print(news_title)


        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)



        news_p= results[0].find('div', class_='rollover_description_inner').text



        #print(news_p)



        url_1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url_1)



        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17302_ip.jpg'



        url_2= 'https://twitter.com/marswxreport?lang=en'
        #response_2 = requests.get(url_2)
        browser.visit(url_2)



        # Create BeautifulSoup object; parse with 'html.parser'
        soup_2 = BeautifulSoup(browser.html, 'html.parser')



        # Examine the results, then determine element that contains sought info
        #print(soup_2)



        mars_weather = soup_2.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        #print(mars_weather)



        url_3 = "https://space-facts.com/mars/"
        tables = pd.read_html(url_3)
        tables



        df = tables[0]
        df.columns = ['Parameter', 'Value']
        df.head()
        

        html_table = df.to_html()
        html_table

        
        url_4= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        url_6= "https://astrogeology.usgs.gov"
        browser.visit(url_4)

        html = browser.html
        soup_4 = BeautifulSoup(html, 'html.parser')

        element = soup_4.find_all('div', class_ = 'item')
        
        for element in element:
            hemisphere= soup.find('h3').text
            print(hemisphere)
        
        for element in element:
            relative_image_path = soup_4.find('img', class_='thumb')['src']
            image_url = url_6 + relative_image_path
            print(image_url) 
        
        data ={
        "news_paragraph" : news_p,
        "news_title" : news_title,
        "featured_image" : featured_image_url,
        "weather" : mars_weather,
        "facts" : html_table,
        "images": image_url
        }

        browser.quit()
        return data
