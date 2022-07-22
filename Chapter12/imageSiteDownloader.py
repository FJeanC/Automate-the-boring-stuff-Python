#! python3
# imageSiteDownloader.py - USE: imageSiteDownloader.py <search query> 
# Download all(?) images related to the specified query from imgur.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import requests, os, bs4, sys
import time
from selenium.common.exceptions import NoSuchElementException


if len(sys.argv) < 2:
    print("The function need more arguments")
else:
    browser = webdriver.Firefox()
    url = 'https://imgur.com/search?q='
    print("Searching page %s" %(url))
    os.makedirs('imgurImages', exist_ok=True)
    Query = ' '.join(sys.argv[1:])
    browser.get(url+Query)
    htmlElem = browser.find_element('tag name', 'html')

    # Find the bottom of the page.
    while True:
        htmlElem.send_keys(Keys.END)
        time.sleep(0.5)
        # If it finds a 'Load More' button, click it.
        try:
            browser.find_element(By.ID, 'load-more')
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "load-more"))).click()
            time.sleep(0.5)
        except NoSuchElementException as e:
            print("Not found")
        
        # If 'nomore' button is found, exit the loop.
        try:
            browser.find_element(By.ID, 'nomore')
            break
        except NoSuchElementException as e:
            print("Not at the end.")

    print("Searching page %s" %(url + Query))
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    linkImgs = soup.select(".image-list-link img") 
    numImgs = len(linkImgs)
    PathImg = 'imgurImages' + Query
    # Only creates a dir if numImgs > 0
    if numImgs > 0:
        try:
            os.mkdir(Query)
        except FileExistsError as err:
            print("File %s already exists. Overwriting it." %Query )
    # Saves the image to a file
    for i in range(numImgs):
        trueLink = linkImgs[i].get('src')[:-5]
        imageUrl = 'https:' + trueLink + '.jpeg'
        print(f"Downloading image N {i}º name:{imageUrl}")
        res = requests.get(imageUrl)
        res.raise_for_status()
        imageFile = open(os.path.join(Query, os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()


