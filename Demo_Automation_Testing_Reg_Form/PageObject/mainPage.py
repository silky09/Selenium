from selenium.webdriver.common.by import By
class MainPage():

    def __init__(self, driver):
        self.driver = driver
        #objects elements-types-locators
        self.firstName_textbox_XPATH = '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input'
        self.lastName_textbox_XPATH = '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input'
        self.address_textarea_XPATH = '//*[@id="basicBootstrapForm"]/div[2]/div/textarea'

        self.gmailAddress_textbox_XPATH = '//body/section[@id="section"]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]'
        self.phoneNumber_textbox_XPATH = "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        self.genderFemale_radioButton_XPATH = "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/label[2]/input[1]"

        self.hobbiesCricket_checkbox_ID = "checkbox1"
        self.hobbiesMovies_checkbox_ID = "checkbox2"

        self.skills_dropdown_XPATH = "//*[@id='Skills']/option[65]"

        self.selectCountry_dropdown_XPATH = "//*[@id='basicBootstrapForm']/div[10]/div/span/span[1]/span"
        self.selectDenmarkCountry_dropdown_XPATH = "//*[@id='select2-country-results']/li[4]"

        self.DOB_year_dropdown_XPATH = "//*[@id='yearbox']/option[66]"
        self.DOB_month_dropdown_XPATH = "//*[@id='basicBootstrapForm']/div[11]/div[2]/select/option[3]"
        self.DOB_day_dropdown_XPATH = "//*[@id='daybox']/option[10]"

        self.password_textbox_ID = 'firstpassword'
        self.confirmPassword_textbox_ID = 'secondpassword'

        self.uploadFile_file_ID = "imagesrc"

        self.refresh_button_ID = 'Button1'

    def enter_firstName(self, firstName):
        driver = self.driver
        driver.find_element(By.XPATH, self.firstName_textbox_XPATH).send_keys(firstName)

    def enter_lastName(self, lastName):
        self.driver.find_element(By.XPATH, self.lastName_textbox_XPATH).send_keys(lastName)

    def enter_address(self, address):
        self.driver.find_element(By.XPATH, self.address_textarea_XPATH).clear()
        self.driver.find_element(By.XPATH, self.address_textarea_XPATH).send_keys(address)

    #//*[@id="eid"]/input
    def enter_gmailAddress(self, gmailAddress):
        self.driver.find_element(By.XPATH, self.gmailAddress_textbox_XPATH).send_keys(gmailAddress)

    def enter_phoneNumber(self, phoneNumber):
        self.driver.find_element(By.XPATH, self.phoneNumber_textbox_XPATH).send_keys(phoneNumber)

    def click_genderFemale(self):
        self.driver.find_element(By.XPATH, self.genderFemale_radioButton_XPATH).click()

    def click_hobbiesCricket(self):
        self.driver.find_element(By.ID, self.hobbiesCricket_checkbox_ID ).click()

    def click_hobbiesMovies(self):
        self.driver.find_element(By.ID, self.hobbiesMovies_checkbox_ID).click()

    def select_software_skill(self):
        self.driver.find_element(By.XPATH, self.skills_dropdown_XPATH).click()

    def select_country(self):
        self.driver.find_element(By.XPATH, self.selectCountry_dropdown_XPATH).click()

    def select_denmarkCountry(self):
        self.driver.find_element(By.XPATH, self.selectDenmarkCountry_dropdown_XPATH).click()

    def select_year(self):
        self.driver.find_element(By.XPATH, self.DOB_year_dropdown_XPATH).click()

    def select_month(self):
        self.driver.find_element(By.XPATH,  self.DOB_month_dropdown_XPATH).click()

    def select_day(self):
        self.driver.find_element(By.XPATH, self.DOB_day_dropdown_XPATH).click()

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_ID).send_keys(password)

    def enter_confirmPassword(self, confirmPassword):
        self.driver.find_element(By.ID, self.confirmPassword_textbox_ID).send_keys(confirmPassword)

    def select_file(self, file):
        self.driver.find_element(By.ID, self.uploadFile_file_ID).send_keys(file)

    def click_refreshButton(self):
        self.driver.find_element(By.ID,  self.refresh_button_ID).click()
