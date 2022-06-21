from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome(executable_path="/Users/thomashoward/Desktop/chromedriver")
driver.get("https://www.espn.com")

#Code for login
login = driver.find_element(By.LINK_TEXT, "MLB").click()




driver.close()



