import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
"""from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC"""
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class formTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_form_valid(self):
        driver = self.driver

        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

        print("Title of the page: ", driver.title)
        print("URL of the page: ", driver.current_url)

        #consent = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
        #consent.click()
        First_Name = driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[1]/td[2]/input")
        First_Name.send_keys("swe")
        Last_Name = driver.find_element(By.XPATH,
                                        "//body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]")
        Last_Name.send_keys("Den")

        Gender = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[3]/td[2]/input[2]")
        Gender.click()
        Exp = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[4]/td[2]/span[5]/input")
        Exp.click()

        Date = driver.find_element(By.XPATH,
                                   "//body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[2]/input[1]")
        Date.send_keys("17/12/2021")
        # profession : checkboxes are not clickable Skip for now

        # Manual_tester = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[6]/td[2]/span[1]/input")
        # Manual_tester.click()

        # Automation_tester = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[4]/div[1]/form[1]/table[1]/tbody[1]/tr[6]/td[2]/span[2]/input[1]")
        # Automation_tester.click()

        # Choose file
        Choose_File = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[7]/td[2]/input")
        Choose_File.send_keys("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")

        # Flavours_of_selenium = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[8]/td[2]/span[3]/input")
        # Flavours_of_selenium.click()

        # Continents using Select and click method
        Continents = Select(driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[9]/td[2]/select"))
        Continents.select_by_visible_text("Europe")

        """Continents = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[9]/td[2]/select/option[2]")
        Continents.click()"""

        # Selenium Commands used both click and Select method : Select only works with select option. so write path of select not others
        """Selenium_Commands = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[10]/td[2]/select/option[5]")
        Selenium_Commands.click()"""

        Selenium_Commands = Select(driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[10]/td[2]/select"))
        Selenium_Commands.select_by_visible_text("WebElement Commands")

        Button = driver.find_element(By.XPATH,
                                     "/html/body/div[1]/div/div[2]/div[4]/div/form/table/tbody/tr[11]/td[2]/button")
        Button.click()

    @classmethod
    def tearDownClass(cls):
        #time.sleep(2)
        # handling with popup
        cls.driver.switch_to.alert.accept()
        cls.driver.quit()
        print("testing done!")


if __name__ == '__main__':
    unittest.main()



