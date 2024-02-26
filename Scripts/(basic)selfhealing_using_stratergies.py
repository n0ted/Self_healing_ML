from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def init_driver():
    # Initialize Selenium WebDriver (you might need to specify the path to your browser driver)
    driver = webdriver.Chrome()
    return driver

def find_button(driver):
    # Find the button by iterating through multiple possible locator strategies
    locator_strategies = [By.ID, By.CLASS_NAME, By.NAME, By.XPATH, By.CSS_SELECTOR]  # Add more strategies as needed
    
    for strategy in locator_strategies:
        try:
            button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((strategy, 'buttonA')))
            return button
        except:
            continue
    
    print("Button not found. Attempting to recover...")
    return None

def increment_counter(driver):
    # Click the button to increment the counter
    button = find_button(driver)
    if button:
        button.click()
    else:
        print("Failed to increment counter")

def main():
    driver = init_driver()
    driver.get('http://127.0.0.1:5500/Website/index.html')  # Replace with the path to your local HTML file

    try:
        while True:
            # Example automation: Increment the counter every 5 seconds
            increment_counter(driver)
            time.sleep(5)

    except KeyboardInterrupt:
        print("Script interrupted.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
