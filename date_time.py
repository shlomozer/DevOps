from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\zers1\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://translate.google.co.il/?hl=iw&tab=wT1")

print(driver.current_url)
driver.find_element_by_id("sources").click()

driver.find_element_by_id("mytextarea").clear()
driver.find_element_by_id("mytextarea").send_keys("hello")

my_element=driver.find_element_by_id("sources")
print(my_element.is_enabled)

driver.find_element_by_id("source").send_keys(keys.ENTER)

