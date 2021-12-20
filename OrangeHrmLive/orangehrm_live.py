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

#Click Admin
driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]').click()

#click username multi Checkboxes
driver.find_element(By.ID, 'ohrmList_chkSelectRecord_46').click()
driver.find_element(By.ID, 'ohrmList_chkSelectRecord_39').click()
driver.find_element(By.ID, 'ohrmList_chkSelectRecord_38').click()
driver.find_element(By.ID, 'ohrmList_chkSelectRecord_33').click()
driver.find_element(By.XPATH, '//*[@id="ohrmList_chkSelectRecord_23"]').click()


#PIM
driver.find_element(By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[2]').click()
driver.find_element(By.XPATH, '//*[@id="ohrmList_chkSelectRecord_64"]').click()


#time.sleep(5)
#Logout
driver.find_element(By.ID, 'welcome').click()
driver.find_element(By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]').click()

#time.sleep(5)
driver.quit()
print("Testing done!")