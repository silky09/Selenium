from selenium.webdriver.common.by import By
class MainPage():
    def __init__(self, driver):
        self.driver = driver

        self.firstName_textbox_ID = 'firstname'
        self.lastName_textbox_ID = 'lastname'
        self.email_textbox_ID = 'email'
        self.gender_radioButton_XPATH = '//*[@id="post-253"]/div[2]/form/fieldset/input[4]'
        self.profession_checkbox_XPATH = "//*[@id='post-253']/div[2]/form/fieldset/input[7]"
        self.selectCountry_dropDown_XPATH = "//*[@id='post-253']/div[2]/form/fieldset/select/option[2]"
        self.skills_dropDown_XPATH = "//*[@id='skillsmultiple']/option[2]"
        self.clickToGetAlert_button_ID = 'alertbutton'


    def enter_firstName(self, firstName):
        self.driver.find_element(By.ID, self.firstName_textbox_ID).send_keys(firstName)

    def enter_lastName(self, lastName):
        self.driver.find_element(By.ID,  self.lastName_textbox_ID).send_keys(lastName)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_ID).send_keys(email)

    def select_genderMale(self):
        self.driver.find_element(By.XPATH, self.gender_radioButton_XPATH).click()

    def select_WorkingProfession(self):
        self.driver.find_element(By.XPATH, self.profession_checkbox_XPATH).click()

    def select_USA_country(self):
        self.driver.find_element(By.XPATH, self.selectCountry_dropDown_XPATH).click()

    def select_skills_AutomationTesting(self):
        self.driver.find_element(By.XPATH, self.skills_dropDown_XPATH).click()

    def click_clickHereToGetAlertButton(self):
        self.driver.find_element(By.ID, self.clickToGetAlert_button_ID).click()



