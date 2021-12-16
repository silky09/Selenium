#imp commands
import time

from selenium import webdriver
#install pip install webdriver-manager in the terminal
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()


time.sleep(10)
#driver.minimize_window()

driver.quit()
print("Testing done and refreshed instead of submit the form!!👏👏")






