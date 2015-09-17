import time
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../../")
import utils

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
	time.sleep(5)
	cpath = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
	if utils.IsWindows():
		cpath = cpath[0].upper() + cpath[1:]
		cpath = '/' + cpath
	assert(driver.current_url == "file://" + cpath + "/index.html")

finally:
    driver.quit()