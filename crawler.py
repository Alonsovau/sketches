from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
from urllib import request


browser = webdriver.Chrome(executable_path='/Users/zhouxin/Downloads/chromedriver')
browser.get('https://www.instagram.com/')
# assert 'Python' in browser.title
# elem = browser.find_element_by_name('q')  # Find the search box
# elem.send_keys('pycon' + Keys.RETURN)
login = browser.find_elements_by_class_name('_b93kq')[0]
login.click()
username = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/'
                                         'div[1]/div/input')
print(username.get_attribute('placeholder'))
username.send_keys('1017092687@qq.com')
passwd = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/'
                                       'div[2]/div/input')
passwd.send_keys('wasd123123')
login = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')
login.click()
time.sleep(1)
login_status = 0
try:
    print(browser.find_element_by_id('slfErrorAlert').text)
except NoSuchElementException:
    print('login ok')
    login_status = 1
time.sleep(3)
if login_status == 1:
    # soup = BeautifulSoup(browser.page_source, 'html.parser')
    # piclist = soup.find_all('img', class_="_2di5p")
    # for p in piclist:
    #     print(p)
    jsondata = browser.find_elements_by_xpath('/html/body/script[1]')
    print(jsondata)
with open('ins.html', 'w') as f:
    f.write(browser.page_source)

# browser.quit()
