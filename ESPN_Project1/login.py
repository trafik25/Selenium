from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome(executable_path="/Users/thomashoward/Desktop/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Code for login
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys('Thomas')
driver.find_element(By.NAME, "email").send_keys('thomashoward206@gmail.com')
driver.find_element(By.ID,"exampleInputPassword1").send_keys("tiesto25")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@value='Submit']")

#using CSS Selector > Console Tools, Clear everything --EXAMPLE $("input[name='name']")
#driver.find_element(By.CSS_SELECTOR)

driver.close()



