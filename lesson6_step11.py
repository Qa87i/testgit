from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".first_block input.first")
    input1.send_keys("I")
    input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
    input2.send_keys("II")
    input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
    input3.send_keys("III")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()