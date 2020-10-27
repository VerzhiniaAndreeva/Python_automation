from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Common.driver_initialize import DriverInitialize
import Tests

base_URL = DriverInitialize.getJsonFileAttributeValue(Tests.test_Settings, "instance")

driver = webdriver.Firefox()
driver.get(base_URL)
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get(base_URL)
myDynamicElement = driver.find_element_by_id("myDynamicElement")

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if somepredicate(*args, **kwargs): return True
        time.sleep(period)
    return False

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'element')))