from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    c = str(int(a) + int(b))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(c)
    button = browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()