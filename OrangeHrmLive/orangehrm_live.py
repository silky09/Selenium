import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

#get the page through url
driver.get("https://opensource-demo.orangehrmlive.com/")

#maximize window
driver.maximize_window()

#title of the page
print("Title of the page: ", driver.title)
#driver.implicitly_wait(10)

#Login panel
driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
driver.find_element(By.ID, 'btnLogin').click()
#Logout
driver.find_element(By.ID, 'welcome').click()
driver.find_element(By.XPATH, '//*[@id="welcome-menu"]/ul/li[3]').click()

time.sleep(5)
driver.quit()
print("Testing done!")