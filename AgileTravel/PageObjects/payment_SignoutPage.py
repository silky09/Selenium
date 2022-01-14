from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class PaymentAndSignout():

    def __init__(self, driver):
        self.driver = driver
        self.visaCard_RadioButton_XPATH = '//*[@id="payment-form"]/table/tbody/tr[1]/td[2]/input[1]'
        self.card_holder_name_textbox_XPATH = '//*[@id="payment-form"]/table/tbody/tr[2]/td[2]/input'
        self.card_number_textbox_XPATH = '//*[@id="payment-form"]/table/tbody/tr[3]/td[2]/input'
        self.expiry_date_XPATH = '//*[@id="payment-form"]/table/tbody/tr[4]/td[2]/select[1]'
        self.expiry_year_XPATH = '//*[@id="payment-form"]/table/tbody/tr[4]/td[2]/select[2]'
        self.payNow_button_XPATH = '//*[@id="payment-form"]/p/input'
        self.signOff_linkText_XPATH = '//*[@id="user_nav"]/a'

    def select_Visa_card_type(self):
        self.driver.find_element(By.XPATH, self.visaCard_RadioButton_XPATH).click()

    def enter_Card_holderName(self, Name):
        self.driver.find_element(By.XPATH, self.card_holder_name_textbox_XPATH).clear()
        self.driver.find_element(By.XPATH, self.card_holder_name_textbox_XPATH).send_keys(Name)

    def enter_CardNumber(self, Number):
        self.driver.find_element(By.XPATH, self.card_number_textbox_XPATH).send_keys(Number)

    def select_Expiry_Date(self, Date):
        Select(self.driver.find_element(By.XPATH, self.expiry_date_XPATH)).select_by_visible_text(Date)

    def select_Expiry_Year(self, Year):
        Select(self.driver.find_element(By.XPATH, self.expiry_year_XPATH)).select_by_visible_text(Year)

    def click_Pay_Now(self):
        self.driver.find_element(By.XPATH, self.payNow_button_XPATH).click()

    def click_SignOff(self):
        self.driver.find_element(By.XPATH, self.signOff_linkText_XPATH ).click()
