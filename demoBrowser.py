from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome driver - Chrome vyhledávač

service_obj = Service()  #vytvořený objekt pro službu Service
driver = webdriver.Chrome(service=service_obj) #zadávám kde se nachází služba ovladače Chrome
driver.maximize_window() #maximalizuje se okno
driver.get("https://rahulshettyacademy.com") #driver se chce dostat na stránku RahulShetty#
print(driver.title) #název karty prohlížeče
print(driver.current_url) #získá aktuální adresu URL
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()


#jak zpracovat statické rozbalovací nabídky pomocí selenium python