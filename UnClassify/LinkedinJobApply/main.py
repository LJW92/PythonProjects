from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3712133571&f_AL=true&f_E=1%2C2&geoId=101452733&keywords" \
      "=python%20developer&location=Australia&refresh=true"


def abort_application():
    # Click Close Button
    close_button_ = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button_.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrom_options)
driver.get(URL)
driver.maximize_window()

time.sleep(2)
login = driver.find_element(By.XPATH, value='/html/body/div[4]/a[1]')
login.click()

time.sleep(2)
email = driver.find_element(By.ID, value="username")
email.send_keys(f'{os.environ.get("EMAIL")}')
password = driver.find_element(By.ID, value="password")
password.send_keys(f'{os.environ.get("PASSWORD")}')
password.send_keys(Keys.ENTER)

time.sleep(2)
# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("0450000000")

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
