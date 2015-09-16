import time
import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("app-path=" + os.path.dirname(os.path.abspath(__file__)))
os.environ["BREAKPAD_DUMP_LOCATION"] = os.path.dirname(os.path.abspath(__file__)) + "/crash"

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
try:
	time.sleep(5)
	assert(os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/crash"))
	files=os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/crash")
	assert(len(files)>0)
	
finally:
	driver.quit()
	del os.environ["BREAKPAD_DUMP_LOCATION"]
	if platform.system() == 'win32':
		os.popen("rd/s/q \"" + os.path.dirname(os.path.abspath(__file__)) + "/crash\"")
	else:
		os.popen("rm -rf \"" + os.path.dirname(os.path.abspath(__file__)) + "/crash\"")
