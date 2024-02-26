import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

class TestSampleWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5500/Website/index.html") 

    def tearDown(self):
        self.driver.quit()

    def test_increment_counter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "counter")))
        initial_value = int(self.driver.find_element(By.ID, "counter").text)
        
        button_a = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "buttonA")))
        button_a.click()
        
        updated_value = int(self.driver.find_element(By.ID, "counter").text)
        self.assertEqual(updated_value, initial_value + 2, "Counter did not increment by 2")
        time.sleep(10)

    def test_decrement_counter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "counter")))
        initial_value = int(self.driver.find_element(By.ID, "counter").text)
        
        button_b = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "buttonB")))
        button_b.click()
        
        updated_value = int(self.driver.find_element(By.ID, "counter").text)
        self.assertEqual(updated_value, initial_value - 1, "Counter did not decrement by 1")
        time.sleep(10)
    def test_submit_name(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameInput")))
        name_input = self.driver.find_element(By.ID, "nameInput")
        name_input.send_keys("John")

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "submitName")))
        submit_button.click()
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameDisplayArea")))
        name_display_area = self.driver.find_element(By.ID, "nameDisplayArea")
        new_name_div = name_display_area.find_element(By.XPATH, "//div[text()='John']")
        self.assertIsNotNone(new_name_div, "Submitted name not displayed")
        time.sleep(10)

    def test_clear_names(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameInput")))
        name_input = self.driver.find_element(By.ID, "nameInput")
        name_input.send_keys("John")
        time.sleep(2)
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "submitName")))
        submit_button.click()
        
        clear_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "clearNames")))
        clear_button.click()
        
        name_display_area = self.driver.find_element(By.ID, "nameDisplayArea")
        self.assertFalse(name_display_area.find_elements(By.TAG_NAME, "div"), "Names not cleared")
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
