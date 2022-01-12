
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
#2
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from Selenium_Practice_Form.PageObjects.mainPage import MainPage
import HtmlTestRunner


class FormTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_form_validity(self):
        driver = self.driver
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

        myDetais = MainPage(driver)
        myDetais.enter_firstName("Swed")
        myDetais.enter_lastName("Denmark")
        myDetais.enter_phone("0987654321")
        myDetais.enter_country("Sweden")
        myDetais.enter_city("Malmö")
        myDetais.enter_email("s@gmail.com")
        myDetais.select_female_Gender()
        myDetais.select_Monday_available()
        myDetais.select_Tuesday_available()
        myDetais.select_Wednesday_available()
        myDetais.select_Friday_available()
        myDetais.select_time_to_connect("Morning")
        myDetais.upload_file("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")
        myDetais.click_SubmitButton()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()
        print("Form submitted!!")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/SeleniumDemoProject/Selenium_Practice_Form/HTML_Reports"))





