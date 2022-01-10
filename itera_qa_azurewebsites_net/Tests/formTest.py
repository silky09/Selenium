import time
import unittest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from itera_qa_azurewebsites_net.PageObjects.homePage import HomePage
import HtmlTestRunner

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
        myInfo = HomePage(driver)
        myInfo.enter_Name("Swen")
        myInfo.enter_Mobile_number("0987654321")
        myInfo.enter_Email("Swe@gmail.com")
        myInfo.enter_Password("Swe123")
        myInfo.enter_Address("Sweden")
        myInfo.click_SubmitButton()

        myInfo.select_femaleGender()
        myInfo.select_Monday_to_startWork()
        myInfo.select_Wednesday_to_startWork()
        myInfo.select_Thursday_to_startWork()
        myInfo.select_Saturday_to_startWork()

        myInfo.select_Denmark_to_travel("Denmark")

        myInfo.select_twoYearsOfExperience()

        myInfo.select_framework_Selenium_Webdriver()
        myInfo.select_framework_TestNG()
        myInfo.select_framework_Testim()

        myInfo.upload_file("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")



    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()
        print("Form automated!!")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/SeleniumDemoProject/itera_qa_azurewebsites_net/Reports"))



