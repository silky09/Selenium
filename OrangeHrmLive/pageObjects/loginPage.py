from selenium.webdriver.common.by import By
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
#objects-types-locators
        self.username_textbox_ID = 'txtUsername'
        self.password_textbox_ID = 'txtPassword'
        self.login_button_ID = 'btnLogin'
#new function for action method
    #for username
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_ID).clear()
        self.driver.find_element(By.ID, self.username_textbox_ID).send_keys(username)

    # for password
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_ID).clear()
        self.driver.find_element(By.ID,  self.password_textbox_ID).send_keys(password)

    # for click button

    def click_login(self):
        self.driver.find_element(By.ID, 'btnLogin').click()