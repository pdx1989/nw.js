import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
	time.sleep(5)
	cpath = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
	if not cpath[0] == '/':
		cpath = '/' + cpath
	assert(driver.current_url == "file://" + cpath + "/index.html")

finally:
    driver.quit()