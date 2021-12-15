import time

from selenium import webdriver
#install pip install webdriver-manager in the terminal
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
#info
driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys("Swe")
driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys("den")
driver.find_element(By.XPATH, '//body/section[@id="section"]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]').send_keys("Malmö")
driver.find_element(By.XPATH, '//body/section[@id="section"]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]').send_keys("S@gmail.com")
driver.find_element(By.XPATH, "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]").send_keys("0123456789")
#Gender
driver.find_element(By.XPATH, "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/label[2]/input[1]").click()
#Hobbies
driver.find_element(By.ID, "checkbox1").click()
driver.find_element(By.ID, "checkbox2").click()

#driver.find_element(By.ID, "msdd").click()
#driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li[8]").click()
#driver.find_element(By.XPATH, "//a[contains(text(),'Swedish')]").click()
#//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]
#//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[8]/a

#select skills
driver.find_element(By.ID, "Skills").click()
#click dropdown list and choose and select item then inspect it separately
driver.find_element(By.XPATH, "//*[@id='Skills']/option[65]").click()

#select country
driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[10]/div/span/span[1]/span").click()
#click dropdown list and choose and select item then inspect it separately
driver.find_element(By.XPATH, "//*[@id='select2-country-results']/li[4]").click()


#DOB
driver.find_element(By.XPATH, "//*[@id='yearbox']/option[66]").click()
driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[11]/div[2]/select/option[3]").click()
driver.find_element(By.XPATH, "//*[@id='daybox']/option[10]").click()

#password
driver.find_element(By.ID, "firstpassword").send_keys("123456789")
driver.find_element(By.ID, "secondpassword").send_keys("123456789")
time.sleep(2)
#Refresh
driver.find_element(By.ID, "Button1").click()

time.sleep(5)
#driver.minimize_window()

driver.quit()
print("Testing done and refreshed instead of submit the form!!👏👏")






