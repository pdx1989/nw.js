import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))
chrome_options.add_argument("nwjs-log-file=" + os.path.dirname(os.path.abspath(__file__)) + "/a.log")
chrome_options.add_argument("enable-logging")

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
    time.sleep(5)
    assert(os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/a.log"))

finally:
    driver.quit()
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/a.log"):
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "/a.log")
