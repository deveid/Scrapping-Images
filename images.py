
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
site='https://www.123rf.com/viewsharedlightbox.php?sharedlightid=1b75e802aa617b5bbe3c151646d5515f&utm_source=0617LikeBox_Share&utm_medium=newsletter&utm_campaign=automailer'
driver = webdriver.Chrome(executable_path='C:/Users/Byteworks/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(site)

# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-widget-content jqgrow ui-row-ltr')))
# except TimeoutException:
#     print('Page timed out after 10 secs.')
    
all_imgs=[]
soup = BeautifulSoup(driver.page_source, 'html.parser')

    
tags = soup.find('div', attrs={"class" : "img_thumbs_container"})
    
for i in tags.find_all("div" , attrs={"class" : "thumb-container"}):
    all_imgs.append(i)
        
img_soup = BeautifulSoup(str(all_imgs),'html.parser')
all_images_link=[]
for img in img_soup.find_all("img"):
    all_images_link.append(img['src'])

filename=all_images_link
for url in all_images_link:
    save1=str(url.split("/")[4])
    save2=str(url.split("/")[5])
    save_name=save1+save2+str(random.randint(1,100))+'.jpg'
    print(save_name)
    with open(save_name, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)
        print(f)
                
for i in range(0,10):  
    all_imgs=[]

    try:
        # Go to page 2
        next_link = driver.find_element_by_xpath("//div[@class='ui tertiary button big-next-button margin-tiny vertical-top']")
        next_link.click()
        index = 0

        # update html and soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

    
        tags = soup.find('div', attrs={"class" : "img_thumbs_container"})
    
        for i in tags.find_all("div" , attrs={"class" : "thumb-container"}):
            all_imgs.append(i)
        
        img_soup = BeautifulSoup(str(all_imgs),'html.parser')
        all_images_link=[]
        for img in img_soup.find_all("img"):
            all_images_link.append(img['src'])

        filename=all_images_link
        for url in all_images_link:
            save1=str(url.split("/")[4])
            save2=str(url.split("/")[5])
            save_name=save1+save2+str(random.randint(1,100))+'.jpg'
            print(save_name)
            with open(save_name, 'wb') as f:
                response = requests.get(url)
                f.write(response.content)
                print(f)
        time.sleep(3)

    except NoSuchElementException:
        rows_remaining = False
    
driver.quit()
