import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))
chrome_options.add_argument("enable-logging")
os.environ["NWJS_LOG_FILE"]=os.path.dirname(os.path.abspath(__file__)) + "/b.log"

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
    time.sleep(5)
    assert(os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/b.log"))

finally:
    driver.quit()
    del os.environ["NWJS_LOG_FILE"]
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/b.log"):
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "/b.log")
