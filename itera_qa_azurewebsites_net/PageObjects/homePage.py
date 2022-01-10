from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.Name_textbox_ID = 'name'
        self.MobileNumber_textbox_ID = 'phone'
        self.Email_textbox_ID = 'email'
        self.Password_textbox_ID = 'password'
        self.Address_textarea_ID = 'address'
        self.Submit_button_XPATH = "/html/body/div/div[2]/div[2]/button"

        #checkbox and radio button practice
        self.femaleGender_radioButton_XPATH = "//input[@id='female']"
        self.Monday_checkbox_XPATH = "//input[@id='monday']"
        self.Wednesday_checkbox_XPATH = "//input[@id='wednesday']"
        self.Thursday_checkbox_XPATH = "//input[@id='thursday']"
        self.Saturday_checkbox_XPATH = "//input[@id='saturday']"

        #dropdown and radio button practice

        self.planToTravel_dropDown_XPATH = '/html/body/div/div[4]/div[2]/div/select'

        self.yearOfExperience_radioButton_XPATH = "/html/body/div/div[5]/div[2]/div[1]/div[2]/label"

        self.frameworkSelenium_checkbox_XPATH = "/html/body/div/div[5]/div[2]/div[2]/div[1]/label"
        self.frameworkTestNG_checkbox_XPATH = "/html/body/div/div[5]/div[2]/div[2]/div[3]/label"
        self.frameworkTestim_checkbox_XPATH = "/html/body/div/div[5]/div[2]/div[2]/div[6]/label"

        self.upload_file_ID = 'inputGroupFile02'

    def enter_Name(self, Name):
        self.driver.find_element(By.ID, self.Name_textbox_ID).send_keys(Name)

    def enter_Mobile_number(self, Mobile_number):
        self.driver.find_element(By.ID, self.MobileNumber_textbox_ID).send_keys(Mobile_number)

    def enter_Email(self, Email):
        self.driver.find_element(By.ID, self.Email_textbox_ID).send_keys(Email)

    def enter_Password(self, Password):
        self.driver.find_element(By.ID, self.Password_textbox_ID).send_keys(Password)

    def enter_Address(self, Address):
        self.driver.find_element(By.ID, self.Address_textarea_ID).send_keys(Address)

    def click_SubmitButton(self):
        self.driver.find_element(By.XPATH, self.Submit_button_XPATH).click()


    def select_femaleGender(self):
        self.driver.find_element(By.XPATH, self.femaleGender_radioButton_XPATH).click()

    def select_Monday_to_startWork(self):
        self.driver.find_element(By.XPATH, self.Monday_checkbox_XPATH).click()

    def select_Wednesday_to_startWork(self):
        self.driver.find_element(By.XPATH, self.Wednesday_checkbox_XPATH).click()

    def select_Thursday_to_startWork(self):
        self.driver.find_element(By.XPATH, self.Thursday_checkbox_XPATH).click()

    def select_Saturday_to_startWork(self):
        self.driver.find_element(By.XPATH, self.Saturday_checkbox_XPATH).click()

    def select_Denmark_to_travel(self, Denmark):
        Select(self.driver.find_element(By.XPATH, self.planToTravel_dropDown_XPATH)).select_by_visible_text(Denmark)

    def select_twoYearsOfExperience(self):
        self.driver.find_element(By.XPATH, self.yearOfExperience_radioButton_XPATH).click()

    def select_framework_Selenium_Webdriver(self):
        self.driver.find_element(By.XPATH, self.frameworkSelenium_checkbox_XPATH).click()

    def select_framework_TestNG(self):
        self.driver.find_element(By.XPATH, self.frameworkTestNG_checkbox_XPATH).click()

    def select_framework_Testim(self):
        self.driver.find_element(By.XPATH, self.frameworkTestim_checkbox_XPATH).click()

    def upload_file(self, file):
        self.driver.find_element(By.ID, self.upload_file_ID).send_keys(file)




