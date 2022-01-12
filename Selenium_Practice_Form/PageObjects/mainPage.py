from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MainPage():

    def __init__(self, driver):
        self.driver = driver

        self.firstName_textbox_ID = 'RESULT_TextField-1'
        self.lastName_textbox_ID = 'RESULT_TextField-2'
        self.phone_textbox_ID = 'RESULT_TextField-3'
        self.country_textbox_ID = 'RESULT_TextField-4'
        self.city_textbox_ID = 'RESULT_TextField-5'
        self.email_textbox_ID = 'RESULT_TextField-6'
        self.femaleGender_radioButton_XPATH = "//*[@id='q26']/table/tbody/tr[2]/td/label"
        self.monday_available_checkbox_XPATH = "//*[@id='q15']/table/tbody/tr[2]/td"
        self.tuesday_available_checkbox_XPATH = "//*[@id='q15']/table/tbody/tr[3]/td"
        self.wednesday_available_checkbox_XPATH = "//*[@id='q15']/table/tbody/tr[4]/td"
        self.friday_available_checkbox_XPATH = "//*[@id='q15']/table/tbody/tr[6]/td"
        self.morning_bestTime_to_contact_dropdown_XPATH = '//*[@id="RESULT_RadioButton-9"]'
        self.upload_file_XPATH = "//*[@id='RESULT_FileUpload-10']"
        self.submit_button_ID = 'FSsubmit'

    def enter_firstName(self, firstName):
        self.driver.find_element(By.ID, self.firstName_textbox_ID).send_keys(firstName)

    def enter_lastName(self, lastName):
        self.driver.find_element(By.ID, self.lastName_textbox_ID).send_keys(lastName)

    def enter_phone(self, phone):
        self.driver.find_element(By.ID, self.phone_textbox_ID).send_keys(phone)

    def enter_country(self, country):
        self.driver.find_element(By.ID, self.country_textbox_ID).send_keys(country)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.city_textbox_ID).send_keys(city)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_ID).send_keys(email)

    def select_female_Gender(self):
        self.driver.find_element(By.XPATH, self.femaleGender_radioButton_XPATH).click()

    def select_Monday_available(self):
        self.driver.find_element(By.XPATH, self.monday_available_checkbox_XPATH).click()

    def select_Tuesday_available(self):
        self.driver.find_element(By.XPATH, self.tuesday_available_checkbox_XPATH).click()

    def select_Wednesday_available(self):
        self.driver.find_element(By.XPATH, self.wednesday_available_checkbox_XPATH).click()

    def select_Friday_available(self):
        self.driver.find_element(By.XPATH, self.friday_available_checkbox_XPATH).click()

    def select_time_to_connect(self, Best_time):
        Select(self.driver.find_element(By.XPATH, self.morning_bestTime_to_contact_dropdown_XPATH)).select_by_visible_text(Best_time)

    def upload_file(self, file):
        self.driver.find_element(By.XPATH,  self.upload_file_XPATH).send_keys(file)

    def click_SubmitButton(self):
        self.driver.find_element(By.ID, self.submit_button_ID).click()