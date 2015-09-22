import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
    time.sleep(5)
    iframe = driver.find_element_by_id("abc")
    driver.switch_to.frame(iframe)
    driver.find_element_by_id("open").click()
    time.sleep(2)
    driver.find_element_by_id("close").click()
    time.sleep(2)
    assert(len(driver.window_handles) == 1)

finally:
    driver.quit()