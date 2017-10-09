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
if login_status == 1:
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    piclist = soup.find_all('img', class_="_2di5p")
    for p in piclist:
        print(p)
    req = request.Request('https://graph.instagram.com/logging_client_events')
    data = b'access_token=1217981644879628%7C67YRbH29DrLArXEQdmTjcW8Gk8k&message=%7B%22app_id%22%3A%221217981644879628%22%2C%22app_ver%22%3A%221.0%22%2C%22data%22%3A%5B%7B%22time%22%3A1507565031.539%2C%22name%22%3A%22instagram_web_time_spent_bit_array%22%2C%22extra%22%3A%7B%22ig_userid%22%3A5523990446%2C%22qe%22%3A%7B%22deact%22%3A%22launch%22%7D%2C%22tos_id%22%3A%22rz5u4y%22%2C%22start_time%22%3A1507564977%2C%22tos_array%22%3A%5B497%2C4194304%5D%2C%22tos_len%22%3A55%2C%22tos_seq%22%3A16%2C%22tos_cum%22%3A35%2C%22log_time%22%3A1507565031539%2C%22referrer%22%3A%22https%3A%2F%2Fwww.instagram.com%2F%22%2C%22referrer_domain%22%3A%22www.instagram.com%22%2C%22url%22%3A%22%2F%22%7D%7D%5D%2C%22log_type%22%3A%22client_event%22%2C%22seq%22%3A6%2C%22session_id%22%3A%2215f01dea7bb-7519b7%22%2C%22device_id%22%3A%22WduWeQAEAAGbKpu12rqoiCNXJKMA%22%7D'
    with request.urlopen(req, data=data) as f:
        print('Data:', f.read().decode('utf-8'))
with open('ins.html', 'w') as f:
    f.write(browser.page_source)

# browser.quit()
