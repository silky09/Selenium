import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from OrangeHrmLive.pageObjects.loginPage import LoginPage
from OrangeHrmLive.pageObjects.homePage import HomePage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # get the page through url
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # maximize window
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_validity(self):
        # Login panel
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        admin = HomePage(driver)
        admin.click_admin()
        admin.select_aravind_checkbox()
        #admin.select_bhuvan_checkbox()

        time.sleep(2)

        pim = HomePage(driver)
        pim.click_pim()
        time.sleep(2)
        pim.click_reset()

        logout = HomePage(driver)
        logout.click_welcome()
        time.sleep(2)
        logout.click_logout()

        """driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
        driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        driver.find_element(By.ID, 'btnLogin').click()"""

        # Click Admin

        """driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]').click()
        # click username multi Checkboxes
        #click aravind
        driver.find_element(By.ID, 'ohrmList_chkSelectRecord_39').click()
        #click bhuvan
        driver.find_element(By.ID, 'ohrmList_chkSelectRecord_51').click()"""


        # PIM
        #self.driver.find_element(By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[2]').click()

        # click reset button
        #self.driver.find_element(By.ID, 'resetBtn').click()

        # Logout
        #self.driver.find_element(By.ID, 'welcome').click()
        #time.sleep(2)
        #self.driver.find_element(By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]').click()

    @classmethod
    def tearDownClass(cls):
        # time.sleep(5)
        cls.driver.quit()

        # title of the page
        #print("Title of the page: ", cls.driver.title)
        print("Testing done!")


if __name__ == '__main__':
    unittest.main()

# to run in the terminal
# cd C:\Users\santo\PycharmProjects\SeleniumDemoProject\OrangeHrmLive\Test
# python -m unittest loginTest.py (filename)



