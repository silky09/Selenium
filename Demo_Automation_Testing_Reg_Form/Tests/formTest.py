import time
from selenium import webdriver
from Demo_Automation_Testing_Reg_Form.PageObject.mainPage import MainPage
#install pip install webdriver-manager in the terminal
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import HtmlTestRunner

import unittest

class FormTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_form_validity(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/Register.html")
        # info
        fName = MainPage(driver)
        fName.enter_firstName("Swe")

        lName = MainPage(driver)
        lName.enter_lastName("Den")

        homeAddress = MainPage(driver)
        homeAddress.enter_address("Denmark")

        gmail = MainPage(driver)
        gmail.enter_gmailAddress("S@gmail.com")

        phone = MainPage(driver)
        phone.enter_phoneNumber("01234567890")

        gender = MainPage(driver)
        gender.click_genderFemale()

        hobbies_1 = MainPage(driver)
        hobbies_1.click_hobbiesCricket()

        hobbies_2 = MainPage(driver)
        hobbies_2.click_hobbiesMovies()

        skill = MainPage(driver)
        skill.select_software_skill()

        selectCountry = MainPage(driver)
        selectCountry.select_country()

        country = MainPage(driver)
        country.select_denmarkCountry()

        DOB_year = MainPage(driver)
        DOB_year.select_year()

        DOB_month = MainPage(driver)
        DOB_month.select_month()

        DOB_day = MainPage(driver)
        DOB_day.select_day()

        password = MainPage(driver)
        password.enter_password("123456789")

        confirmPassword = MainPage(driver)
        confirmPassword.enter_confirmPassword("123456789")

        upload_file = MainPage(driver)
        upload_file.select_file("C:/Users/santo/PycharmProjects/SeleniumDemoProject/Images/Demo_image.png")

        time.sleep(2)
        refreshButton = MainPage(driver)
        refreshButton.click_refreshButton()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Testing done and refreshed instead of submit the form!!👏👏")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/SeleniumDemoProject/Demo_Automation_Testing_Reg_Form/Reports"))









