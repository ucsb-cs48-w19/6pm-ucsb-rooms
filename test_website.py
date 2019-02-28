import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re
import sys
import pytest

def test_website():
        options = Options()
        options.add_argument("--headless")  #Commented out for testing purposes
        #self.driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),   options=self.options)
        platform = sys.platform

        if (platform == "linux"):
            driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_linux'),   options=options)
        else:
            driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_mac'),   options=options)
        driver.get("https://ucsb-rooms.herokuapp.com/")

        assert None != driver.find_element_by_xpath("//input[@value='Submit']")


        driver.close()


