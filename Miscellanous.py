import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")#SSL certifikat

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options =chrome_options)
driver.implicitly_wait(2)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);") #rolování
driver.get_screenshot_as_file("screen.png")#pořízení screnshotu