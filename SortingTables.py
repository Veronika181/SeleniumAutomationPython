from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []
service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#klikni na záhlaví sloupce
driver.find_element(By.Xpath, "//span[text()='Veg/fruit name']")
#shromáždi všechny názvy zeleniny -> BrowserSortedveggieList (B, A, C),
veggieWebElements = driver.find_element(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

#Shromáždi vše do jednoho seznamu (veggieList) -> newSortedList (A, B, C)
browserSortedVeggies.sort()

assert browserSortedVeggies.sort == originalBrowserSortedList
#veggieList == newSortedList