from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, Xpath, CSSSelector, name, linkText -> lokátory
#Lokátor zjistím přes inspection

driver.find_element(By.NAME, "email").send_keys("hello@gmail.cz")  #najdi prvek a v závorce podle čeho najít prvek a pak jak se jmenuje tento prvek v kodu a pošlu tam věci ,které chci doplnit
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#Pokud chci vytvořit cestu X pro jakýkoliv element tak musím syntaxi napsat jako toto lomítko
# XPATH -př. //tagname[@attribute='value'] ->//input[@type='submit']
# CSS - tagname[attribute='value'] -> //input[@type='submit'] #id, .classname

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()