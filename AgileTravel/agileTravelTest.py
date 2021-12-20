import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

#get the page through url
driver.get("https://travel.agileway.net/login")
#maximize window
driver.maximize_window()

#title of the page
print("Title of the page: ", driver.title)
driver.implicitly_wait(10)

#Login Agile Travel
driver.find_element(By.ID, 'username').send_keys("agileway")
driver.find_element(By.ID, 'password').send_keys("testwise")
#remember_me
driver.find_element(By.ID, 'remember_me').click()
#Sign in
driver.find_element(By.XPATH, '//*[@id="login-box"]/p[4]/input').click()

#Select Flight
#Trip type :Return
driver.find_element(By.XPATH, '//body[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]').click()

#Destination
Origin_From = Select(driver.find_element(By.XPATH, '//*[@id="container"]/form/table[1]/tbody/tr[2]/td[2]/select'))
Origin_From.select_by_visible_text("New York")

Origin_to = Select(driver.find_element(By.XPATH, '//*[@id="container"]/form/table[1]/tbody/tr[3]/td[2]/select'))
Origin_to.select_by_visible_text("Sydney")

#Departing
Departing_Date = Select(driver.find_element(By.XPATH, '//*[@id="departDay"]'))
Departing_Date.select_by_visible_text("09")

Departing_month = Select(driver.find_element(By.XPATH, '//*[@id="departMonth"]'))
Departing_month.select_by_visible_text("Feburary 2021")

#Returning
Returning_Date = Select(driver.find_element(By.XPATH, '//*[@id="returnDay"]'))
Returning_Date.select_by_visible_text("18")


Returning_month = Select(driver.find_element(By.XPATH, '//*[@id="returnMonth"]'))
Returning_month.select_by_visible_text("Feburary 2021")

#click Time	Flight No.	Airline
driver.find_element(By.XPATH, '//*[@id="flights"]/tbody/tr[1]/th/input').click()
driver.find_element(By.XPATH, '//*[@id="flights"]/tbody/tr[3]/th/input').click()

#click Countinue
driver.find_element(By.XPATH, '//*[@id="container"]/form/input').click()

#Passenger detail
driver.find_element(By.XPATH, '//*[@id="container"]/form/table/tbody/tr[1]/td[2]/input').send_keys("S")
driver.find_element(By.XPATH, '//*[@id="container"]/form/table/tbody/tr[2]/td[2]/input').send_keys("San")

driver.find_element(By.XPATH, '//*[@id="container"]/form/input[3]').click()

#Pay by Credit Card
driver.find_element(By.XPATH, '//*[@id="payment-form"]/table/tbody/tr[1]/td[2]/input[1]').click()
driver.find_element(By.XPATH, '//*[@id="payment-form"]/table/tbody/tr[2]/td[2]/input').clear()
driver.find_element(By.XPATH, '//*[@id="payment-form"]/table/tbody/tr[2]/td[2]/input').send_keys("SS")
driver.find_element(By.XPATH, '//*[@id="payment-form"]/table/tbody/tr[3]/td[2]/input').send_keys("12345")

Expiry_in_Date= Select(driver.find_element(By.XPATH, '//*[@id="payment-form"]/table/tbody/tr[4]/td[2]/select[1]'))
Expiry_in_Date.select_by_visible_text("09")


Expiry_in_Month = Select(driver.find_element(By.XPATH, '//*[@id="payment-form"]/table/tbody/tr[4]/td[2]/select[2]'))
Expiry_in_Month.select_by_visible_text("2024")

#pay now
driver.find_element(By.XPATH, '//*[@id="payment-form"]/p/input').click()

time.sleep(6)
#sign off
driver.find_element(By.XPATH, '//*[@id="user_nav"]/a').click()
time.sleep(4)
print("form Automated!")
driver.quit()