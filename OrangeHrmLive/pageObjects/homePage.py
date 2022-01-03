from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    #click admin
        self.admin_link_XPATH = '//*[@id="menu_admin_viewAdminModule"]'
    #select checkboxes
        self.aravind_checkbox_ID = 'ohrmList_chkSelectRecord_39'
        self.bhuvan_checkbox_ID = 'ohrmList_chkSelectRecord_51'

    # click PIM
        self.pim_link_XPATH = '//*[@id="mainMenuFirstLevelUnorderedList"]/li[2]'
        # click reset button
        self.reset_button_ID = 'resetBtn'

    # logout

        self.welcome_link_ID = 'welcome'
        self.logout_link_XPATH = '//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]'

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.admin_link_XPATH).click()

    def select_aravind_checkbox(self):
        self.driver.find_element(By.ID, self.aravind_checkbox_ID).click()

    def select_bhuvan_checkbox(self):
        self.driver.find_element(By.ID,  self.bhuvan_checkbox_ID).click()

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.pim_link_XPATH).click()

    def click_reset(self):
        self.driver.find_element(By.ID,  self.reset_button_ID).click()

    def click_welcome(self):
        self.driver.find_element(By.ID,  self.welcome_link_ID).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_XPATH).click()


