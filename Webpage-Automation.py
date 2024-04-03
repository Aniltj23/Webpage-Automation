from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Providing implicit wait of 5 seconds
mywait=WebDriverWait(driver, 5)

# Maximizing the window
driver.maximize_window()

# Open the registration page
driver.get("https://login.yahoo.com/account/create")

# Type the first name
driver.find_element(By.ID, "usernamereg-firstName").send_keys("Anil")

# Type the last name
driver.find_element(By.NAME, "lastName").send_keys("admin123")

# Type the Username
driver.find_element(By.XPATH, "//input[@id='usernamereg-userId']").send_keys("Anil870")

# Type the Password
driver.find_element(By.XPATH, "//input[@id='usernamereg-password']").send_keys("Testpassword981")

# Click on the date option
driver.find_element(By.XPATH, "//select[@id='usernamereg-month']").click()

# Select 5th month
driver.find_element(By.XPATH, "//option[@value='5']").click() # selecting 5th month

# Give 21 as the day
driver.find_element(By.XPATH, "//input[@id='usernamereg-day']").send_keys("21")

# Give year as 1998
driver.find_element(By.XPATH, "//input[@id='usernamereg-year']").send_keys("1998")

# Save the screenshot of the page
driver.save_screenshot("C:\\Users\\Admin\Pictures\\register.png")

# Print the webpage title
print(driver.title)

# to get time to have a look at the data given
time.sleep(5)

# Verify the webpage title before clicking the submit button
submit = driver.find_element(By.XPATH, "//button[@id='reg-submit-button']")

if driver.title == "Yahoo25":
    submit.click()
else:
    print("Title is wrong")


# Close the current browser window
driver.close()
