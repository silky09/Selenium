import time

from selenium import webdriver
#install pip install webdriver-manager in the terminal
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(5)
driver.quit()
print("Testing done!!")






