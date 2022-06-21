from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome(executable_path="/Users/thomashoward/Desktop/chromedriver")  # driver object
driver = webdriver.Firefox(executable_path="/Users/thomashoward/Desktop/geckodriver")

driver.get("https://www.espn.com")  # get method used for envoking the browser
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.get("https://www.espn.com/mlb/")
driver.back()  # back to homepage of ESPN

driver.close()
