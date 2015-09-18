import time
import os

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
    time.sleep(5)
    elem = driver.find_element_by_id("abc")
    driver.switch_to_frame(elem)
    driver.find_element_by_id("btn").click()
    driver.switch_to_default_content()
    assert(driver.find_element_by_id("success"))

except exceptions.WebDriverException:
    assert(0)

finally:
    driver.quit()