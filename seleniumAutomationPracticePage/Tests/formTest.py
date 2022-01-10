import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from seleniumAutomationPracticePage.PageObjects.mainPage import MainPage
import HtmlTestRunner

class formTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_form_valid(self):
        driver = self.driver
        driver.get("https://automationexplore.com/selenium-automation-practice-page/")
        print(driver.title)

        Info = MainPage(driver)
        Info.enter_firstName("MinSwe")
        Info.enter_lastName("Den")
        Info.enter_email("S@gmail.com")
        Info.select_genderMale()
        Info.select_WorkingProfession()
        Info.select_USA_country()
        Info.select_skills_AutomationTesting()
        Info.click_clickHereToGetAlertButton()

        time.sleep(3)
        # driver.switch_to_alert().accept()

        driver.switch_to.alert.accept()
        # driver.switch_to.alert.dismiss()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

        print("Testing done!")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/SeleniumDemoProject/seleniumAutomationPracticePage/Reports"))







