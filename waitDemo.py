import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5) #globální časový limit pro skript, pokud se na stránce nezobrazí žádný prvek, počká max. 5 sekund než se zobrazí

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber") #pokud je to ID a chci generovat CSS pak hash ID je  nazev třídy
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class= 'products']/div") #seznam[] #jedná se o počet slovesných prvků
count = len(results)
assert count > 0 #měla bych dostat nulové hodnoty zeleniny/ovoce
for result in results:
    result.find_element(By.XPATH, "div/button").click() #jak kliknout na tlačítka, v první iterací se zkontroluje prvek a klikne se
                                                        #ve druhe iteraci se vezme druhý součin

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click() #text se rovná a ja pokračuje ke kontrole
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy") #vypsání promo kodu
driver.find_element(By.CSS_SELECTOR,".promoBtn").click() #promo tlačítko Apply
time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)  #pokud se neshoduje dojde k chybě