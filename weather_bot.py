from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

try:
    driver.get("https://www.example-website.com")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nearby-locations-list")))

    locations = driver.find_elements(By.CSS_SELECTOR, ".nearby-locations-list .nearby-location.weather-card")

    for location in locations:
        city_name = location.find_element(By.CSS_SELECTOR, ".text.title.no-wrap").text
        temperature = location.find_element(By.CSS_SELECTOR, ".text.temp").text
        print(f"{city_name}: {temperature}")

finally:
    driver.quit()
