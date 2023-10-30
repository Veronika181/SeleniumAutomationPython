from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")