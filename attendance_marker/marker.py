from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

# Create tmp_dir
temp_dir = "~/_tmp"
os.makedirs(temp_dir)
os.environ["TMPDIR"] = temp_dir

# Set path to firefox binary
opt = webdriver.FirefoxOptions()
opt.binary_location = "/usr/bin/firefox"
# Set up the WebDriver (use the appropriate driver for your browser, e.g., ChromeDriver)
driver = webdriver.Firefox()

# Open the target page
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=TY8KsmoNLk-Dohgclo-IgqHFTDzolIVCr6BdNSXvvHtUNkZLMzcySkozQjk1T0RNU0RFS1VQWlBBNi4u&origin=Invitation&channel=0")  # Replace with the actual path or URL

try:
    # Locate the checkbox using its `data-automation-value` attribute
    checkbox = driver.find_element(By.XPATH, "//input[@data-automation-value='Aaron Amanor Atter']")

    # Scroll into view if necessary
    ActionChains(driver).move_to_element(checkbox).perform()

    # Check if the checkbox is not already selected, then click to select it
    if not checkbox.is_selected():
        checkbox.click()

    print("Checkbox for 'Aaron Amanor Atter' has been selected.")
except Exception as e:
    print(f"An error occurred: {e}")

# Optionally, keep the browser open for inspection, then close it
input("Press Enter to close the browser...")
driver.quit()
