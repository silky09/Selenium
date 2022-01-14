import time
import unittest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from AgileTravel.PageObjects.loginPage import LoginPage
from AgileTravel.PageObjects.welcomePage import WelcomePage
from AgileTravel.PageObjects.passengerDetailsPage import PassengerDetailPage
from AgileTravel.PageObjects.payment_SignoutPage import PaymentAndSignout
import HtmlTestRunner

class formTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        # maximize window
        cls.driver.maximize_window()

    def test_form_valid(self):
        driver = self.driver

        # get the page through url
        driver.get("https://travel.agileway.net/login")

        login = LoginPage(driver)
        login.enter_UserName("agileway")
        login.enter_Password("testwise")
        login.select_Remember_Me()
        login.click_Sign_in()

        welcome = WelcomePage(driver)
        welcome.select_Return_Trip()
        welcome.select_Origin("Sydney")
        welcome.select_Destination("New York")
        welcome.select_Departing_Date("01")
        welcome.select_Departing_Month("Feburary 2021")
        welcome.select_Returning_Date("01")
        welcome.select_Returning_Month("March 2021")
        welcome.select_Time8()
        welcome.select_Time9()
        welcome.click_Continue()

        passenger = PassengerDetailPage(driver)
        passenger.enter_FirstName("JO")
        passenger.enter_LastName("JO")
        passenger.click_Next()

        payment = PaymentAndSignout(driver)
        payment.select_Visa_card_type()
        payment.enter_Card_holderName("JAYSON")
        payment.enter_CardNumber("121314")
        payment.select_Expiry_Date("09")
        payment.select_Expiry_Year("2025")
        payment.click_Pay_Now()
        payment.click_SignOff()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        print("form Automated!")
        #print("Title of the page: ", driver.title)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/santo/PycharmProjects/Selenium/AgileTravel/Reports"))


