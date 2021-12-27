import time
import unittest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FormTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        #driver = cls.driver
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        # maximize the window
        cls.driver.maximize_window()


    def test_form_validate(self):
        driver = self.driver
        # get the testing page
        driver.get("https://itera-qa.azurewebsites.net/home/automation")

        # print title of the page
        print('title of the page', driver.title)

        # print URL of the page
        print('URL of the page', driver.current_url)

        # Textarea practice
        # Name
        driver.find_element(By.ID, "name").send_keys("Swe")
        # Mob num
        driver.find_element(By.ID, "phone").send_keys("1234567890")
        # Email
        driver.find_element(By.ID, "email").send_keys("Swe@gmail.com")
        # Password
        driver.find_element(By.ID, "password").send_keys("Swe123")
        # Address
        driver.find_element(By.ID, "address").send_keys("Sweden")
        # Submit button
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/button").click()

        # CheckBox & Radio Button practice
        # gender
        driver.find_element(By.XPATH, "//input[@id='female']").click()
        # Which days of the week are best to start something new?
        driver.find_element(By.XPATH, "//input[@id='monday']").click()
        driver.find_element(By.XPATH, "//input[@id='wednesday']").click()
        driver.find_element(By.XPATH, "//input[@id='thursday']").click()
        driver.find_element(By.XPATH, "//input[@id='saturday']").click()

        # DropDown practice
        # Where do you plan to travel this year?
        # use select method

        travel = Select(driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div/select'))
        travel.select_by_visible_text("Denmark")

        # CheckBox & Radio Button practice Xpath
        # Years of experience in test automation

        driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[1]/div[2]/label").click()

        # Which automation tools/frameworks do you use?
        driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div[1]/label").click()
        driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div[3]/label").click()
        driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div[6]/label").click()
        # File input practice
        driver.find_element(By.ID, "inputGroupFile02").send_keys("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()
        print("Form automated!!")


if __name__ == '__main__':
    unittest.main()



