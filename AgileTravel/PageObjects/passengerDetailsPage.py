from selenium.webdriver.common.by import By

class PassengerDetailPage():

    def __init__(self, driver):
        self.driver = driver
        self.firstName_textbox_XPATH = '//*[@id="container"]/form/table/tbody/tr[1]/td[2]/input'
        self.lastName_textbox_XPATH = '//*[@id="container"]/form/table/tbody/tr[2]/td[2]/input'
        self.next_button_XPATH = '//*[@id="container"]/form/input[3]'

    def enter_FirstName(self, FirstName):
        self.driver.find_element(By.XPATH, self.firstName_textbox_XPATH).send_keys(FirstName)

    def enter_LastName(self, LastName):
        self.driver.find_element(By.XPATH, self.lastName_textbox_XPATH).send_keys(LastName)

    def click_Next(self):
        self.driver.find_element(By.XPATH,  self.next_button_XPATH).click()

