import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://automationexplore.com/selenium-automation-practice-page/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)

driver.find_element(By.ID, "firstname").send_keys("Swe")
driver.find_element(By.ID, "lastname").send_keys("Den")
driver.find_element(By.ID, "email").send_keys("S@gmail.com")
driver.find_element(By.XPATH, "//*[@id='post-253']/div[2]/form/fieldset/input[4]").click()
driver.find_element(By.XPATH, "//*[@id='post-253']/div[2]/form/fieldset/input[7]").click()
driver.find_element(By.XPATH, "//*[@id='post-253']/div[2]/form/fieldset/input[8]").click()
driver.find_element(By.XPATH, "//*[@id='post-253']/div[2]/form/fieldset/select/option[2]").click()
driver.find_element(By.XPATH, "//*[@id='skillsmultiple']/option[2]").click()
driver.find_element(By.ID, "alertbutton").click()

time.sleep(3)
#driver.switch_to_alert().accept()

driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()
driver.quit()

print("Testing done!")
