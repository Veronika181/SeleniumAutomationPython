from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") #vyplnění emailové adresy přes inspection
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")  #vyplnění hesla
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello1234") #vyplnění potvrzení hesla
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

