from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to chromedriver executable
chromedriver_path = 'C:/chromedriver-win64/chromedriver.exe'  

# Configure options for Chrome
options = Options()
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')

# Initialize the web driver with the correct path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the website
    driver.get('https://www.facebook.com/login/')

    # Wait until the username and password fields are present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))

    # Find the username and password fields
    username_field = driver.find_element(By.ID, 'email')
    password_field = driver.find_element(By.ID, 'pass')

    # Enter the username and password
    username_field.send_keys('admin')
    password_field.send_keys('admin')

    # Click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # Wait for the login to complete and check for success or failure
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.success-message')))
        print("Login successful!")
    except TimeoutException:
        print("Login failed: Success message not found.")

except TimeoutException:
    print("Loading the page took too much time!")
except NoSuchElementException as e:
    print(f"An element was not found: {e}")

finally:
    # Close the web driver
    driver.quit()