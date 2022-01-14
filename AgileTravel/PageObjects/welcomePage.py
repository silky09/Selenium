from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class WelcomePage():

    def __init__(self, driver):
        self.driver = driver
        self.TripType_return_radioButton_XPATH = '//body[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]'
        self.originNewYork_dropdown_XPATH = '//*[@id="container"]/form/table[1]/tbody/tr[2]/td[2]/select'
        self.destinationSydney_dropdown_XPATH = '//*[@id="container"]/form/table[1]/tbody/tr[3]/td[2]/select'
        self.departingDate_dropdown_XPATH = '//*[@id="departDay"]'
        self.departingMonth_dropdown_XPATH = '//*[@id="departMonth"]'
        self.returningDate_dropdown_XPATH = '//*[@id="returnDay"]'
        self.returningMonth_dropdown_XPATH = '//*[@id="returnMonth"]'
        self.time8_checkbox_XPATH = '//*[@id="flights"]/tbody/tr[1]/th/input'
        self.time9_checkbox_XPATH = '//*[@id="flights"]/tbody/tr[3]/th/input'
        self.continue_button_XPATH = '//*[@id="container"]/form/input'

    def select_Return_Trip(self):
        self.driver.find_element(By.XPATH, self.TripType_return_radioButton_XPATH).click()

    def select_Origin(self, Origin):
        Select(self.driver.find_element(By.XPATH, self.originNewYork_dropdown_XPATH)).select_by_visible_text(Origin)

    def select_Destination(self, Destination):
        Select(self.driver.find_element(By.XPATH, self.destinationSydney_dropdown_XPATH)).select_by_visible_text(Destination)

    def select_Departing_Date(self, Date):
        Select(self.driver.find_element(By.XPATH, self.departingDate_dropdown_XPATH)).select_by_visible_text(Date)

    def select_Departing_Month(self, Month):
        Select(self.driver.find_element(By.XPATH, self.departingMonth_dropdown_XPATH)).select_by_visible_text(Month)

    def select_Returning_Date(self, Date):
        Select(self.driver.find_element(By.XPATH, self.returningDate_dropdown_XPATH)).select_by_visible_text(Date)

    def select_Returning_Month(self, Month):
        Select(self.driver.find_element(By.XPATH, self.returningMonth_dropdown_XPATH)).select_by_visible_text(Month)

    def select_Time8(self):
        self.driver.find_element(By.XPATH, self.time8_checkbox_XPATH).click()

    def select_Time9(self):
        self.driver.find_element(By.XPATH, self.time9_checkbox_XPATH).click()

    def click_Continue(self):
        self. driver.find_element(By.XPATH, self.continue_button_XPATH).click()
