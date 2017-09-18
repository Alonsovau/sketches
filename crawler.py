from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path='/Users/zhouxin/Downloads/chromedriver')
browser.get('http://www.python.org')
assert 'Python' in browser.title
elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys('pycon' + Keys.RETURN)
print(browser.page_source)
browser.quit()
