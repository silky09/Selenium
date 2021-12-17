import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
print("Title of the page: ", driver.title)
print("url of the demo page: ", driver.current_url)
driver.implicitly_wait(10)

driver.find_element(By.ID, "firstName").send_keys("Swe")
driver.find_element(By.ID, "lastName").send_keys("Den")
driver.find_element(By.ID, "userEmail").send_keys("Swe@gmail.com")

driver.find_element(By.XPATH, "//*[@id='genterWrapper']/div[2]/div[2]/label").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")
#DOB box is not clickable skip for now
Subject = driver.find_element(By.ID, "subjectsInput")
Subject.send_keys("Selenium-Python")


time.sleep(1)
#Hobbies skipped not working
#driver.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]").click()
#driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[2]').click()

uploadPic = driver.find_element(By.ID,'uploadPicture')
uploadPic.send_keys("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")

Address = driver.find_element(By.ID,'currentAddress')
Address.send_keys("Sweden!")

Select_city = driver.find_element(By.XPATH, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]')
Select_city.click()
driver.find_element(By.ID, "react-select-3-option-2").click()

driver.find_element(By.XPATH, "//div[@id='city']/div/div[2]/div").click()
driver.find_element(By.ID, "react-select-4-option-1").click()

Submit = driver.find_element(By.ID, 'submit')
Submit.click()

time.sleep(2)
driver.quit()
print("Happy Testing!!")