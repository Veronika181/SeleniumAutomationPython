from os import name

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver) #řetězce akcí
#action.double_click((driver.find_element(By.)) dvojté kliknutí
#action.context_click()
#action.click_and_hold() #dlouhý stisk,podržení
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #ořesune konkrtní prvek
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
