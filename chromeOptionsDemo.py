from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.chromeOptions()
chrome_options.add_argument("--start-maximized")

service_obj = Service(executable_path="/Users/veronikaobrtelova/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(executable_path="\\chromedriver.exe")


driver.get("https://rahulshettyacademy.com/angularpractice/")