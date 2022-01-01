
import time
#1
from selenium import webdriver
from selenium.webdriver.common.by import By
#2
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

#3
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

First_Name = driver.find_element(By.ID, "RESULT_TextField-1")
First_Name.send_keys("Swe")
Last_Name = driver.find_element(By.ID, "RESULT_TextField-2")
Last_Name.send_keys("Den")
Phone_Num = driver.find_element(By.ID, "RESULT_TextField-3")
Phone_Num.send_keys("0987654321")
Country_Name = driver.find_element(By.ID, "RESULT_TextField-4")
Country_Name.send_keys("Sweden")
City_Name = driver.find_element(By.ID, "RESULT_TextField-5")
City_Name.send_keys("Malmö")
Email = driver.find_element(By.ID, "RESULT_TextField-6")
Email.send_keys("S@gmail.com")
Gender = driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[2]/td/label")
Gender.click()
Days_Available = driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[2]/td")
Days_Available.click()
Tue_Available = driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[3]/td")
Tue_Available.click()
Wed_Available = driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[4]/td")
Wed_Available.click()
Fri_Available = driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[6]/td")
Fri_Available.click()

Best_Time_To_Contact = driver.find_element(By.ID, "RESULT_RadioButton-9")
Best_Time_To_Contact.click()
Morning = driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-9']/option[2]")
Morning.click()

Upload_Files = driver.find_element(By.XPATH,"//*[@id='RESULT_FileUpload-10']")
#give the complete path of the file where it is located
Upload_Files.send_keys("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")

Submit = driver.find_element(By.ID,"FSsubmit")
Submit.click()

time.sleep(5)
driver.quit()
print("Form submitted!!")