#
#       August 18, 2021
#
#       Crawling google images using selenium framework
#       Tutorial on JoCoding@Youtube
#



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


#open browser
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.co.kr/imghp?hl=en&authuser=0&ogbl")


#search keyword 
elem = driver.find_element_by_name("q")
elem.send_keys("IU")
elem.send_keys(Keys.RETURN)


#scroll down
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height


#pretend to be a browser (access to bot-forbidden sites)
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


#select and save photo
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count += 1
    except:
        pass


#close browser
driver.close()

