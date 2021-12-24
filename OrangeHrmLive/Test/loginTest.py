import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # get the page through url
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # maximize window
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)




    def test_login_validity(self):
        # Login panel
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, 'txtUsername').send_keys("Admin")
        self.driver.find_element(By.ID, 'txtPassword').send_keys("admin123")
        self.driver.find_element(By.ID, 'btnLogin').click()

        # Click Admin
        self.driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]').click()

        # click username multi Checkboxes
        self.driver.find_element(By.ID, 'ohrmList_chkSelectRecord_46').click()
        self.driver.find_element(By.ID, 'ohrmList_chkSelectRecord_39').click()
        self.driver.find_element(By.ID, 'ohrmList_chkSelectRecord_38').click()
        self.driver.find_element(By.ID, 'ohrmList_chkSelectRecord_33').click()
        self.driver.find_element(By.XPATH, '//*[@id="ohrmList_chkSelectRecord_23"]').click()
        # time.sleep()

        # PIM
        self.driver.find_element(By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[2]').click()

        # Checkboxes
        # driver.find_element(By.ID, 'ohrmList_chkSelectRecord_64').click()
        # driver.find_element(By.XPATH, '//*[@id="ohrmList_chkSelectRecord_68"]').click()
        # driver.find_element(By.XPATH, '//*[@id="ohrmList_chkSelectRecord_54"]').click()

        # time.sleep(3)
        # Logout
        self.driver.find_element(By.ID, 'welcome').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]').click()

    @classmethod
    def tearDownClass(cls) -> None:
        # time.sleep(5)
        cls.driver.quit()

        # title of the page
        #print("Title of the page: ", cls.driver.title)
        print("Testing done!")








