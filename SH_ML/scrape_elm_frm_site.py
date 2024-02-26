import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_current_page(driver, file_path):
    elements = driver.find_elements(By.XPATH, "//*")
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['element', 'tag', 'id', 'type', 'class', 'name', 'aria-autocomplete', 'title', 'href', 'text', 'value', 'aria-label'])
        
        for element in elements:

            element_representation = element.text.strip() if element.text.strip() else element.get_attribute('value') if element.get_attribute('value') else 'None'
            tag = element.tag_name if element.tag_name else 'None'
            element_id = element.get_attribute('id') if element.get_attribute('id') else 'None'
            element_type = element.get_attribute('type') if element.get_attribute('type') else 'None'
            element_class = element.get_attribute('class') if element.get_attribute('class') else 'None'
            name = element.get_attribute('name') if element.get_attribute('name') else 'None'
            aria_autocomplete = element.get_attribute('aria-autocomplete') if element.get_attribute('aria-autocomplete') else 'None'
            title = element.get_attribute('title') if element.get_attribute('title') else 'None'
            href = element.get_attribute('href') if element.get_attribute('href') else 'None'
            text = element.text.strip() if element.text.strip() else 'None'
            value = element.get_attribute('value') if element.get_attribute('value') else 'None'
            aria_label = element.get_attribute('aria-label') if element.get_attribute('aria-label') else 'None'

            writer.writerow([element_representation, tag, element_id, element_type, element_class, name, aria_autocomplete, title, href, text, value, aria_label])

# Usage part
if __name__ == "__main__":
    driver = webdriver.Chrome()  
    driver.get("https://accounts.lambdatest.com/login") 
    scrape_current_page(driver, 'elements.csv')
    driver.quit()
