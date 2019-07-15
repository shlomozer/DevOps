from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zers1\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("shlomo.zer@gmail.com")
driver.find_element_by_id("pass").send_keys("Aa123456").click()









