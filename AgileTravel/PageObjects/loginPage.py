from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.userName_textbox_ID = 'username'
        self.password_textbox_ID = 'password'
        self.rememberMe_checkbox_ID = 'remember_me'
        self.signIn_button_XPATH = '//*[@id="login-box"]/p[4]/input'

    def enter_UserName(self, UserName):
        self.driver.find_element(By.ID, self.userName_textbox_ID).send_keys(UserName)

    def enter_Password(self, Password):
        self.driver.find_element(By.ID, self.password_textbox_ID).send_keys(Password)

    def select_Remember_Me(self):
        self.driver.find_element(By.ID, self.rememberMe_checkbox_ID).click()

    def click_Sign_in(self):
        self.driver.find_element(By.XPATH, self.signIn_button_XPATH).click()
