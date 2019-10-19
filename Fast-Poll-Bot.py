import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
print ("By ojm2015 Github")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument(r"-incognito")	
driver = webdriver.Chrome(executable_path=r'C:\Users\mille\AppData\Roaming\Python\Python35\site-packages\selenium\webdriver\chrome\chromedriver.exe', chrome_options=chrome_options)
driver.get('https://fast-poll.com/poll/950987e6')
time.sleep(2)
CookieAgree = driver.find_element_by_xpath("//button[@id='gdpr-cookie-accept'][1]")
CookieAgree.click()
time.sleep(2)
vote = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/form/div[1]/label")
vote.click()
submitvote = driver.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/form/div[4]/button")
submitvote.click()
driver.quit() 
