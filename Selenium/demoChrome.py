from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/thomashoward/Desktop/chromedriver")  # driver object

driver.get("https://www.espn.com")  #get method used for envoking the browser
driver.close()
