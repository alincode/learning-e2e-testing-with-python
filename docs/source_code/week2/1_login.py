from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
assert "OrangeHRM" in driver.title

driver.maximize_window()

try:
    user_name = driver.find_element_by_css_selector("#txtUsername")
    user_name.send_keys("Admin")

    user_email = driver.find_element_by_css_selector("#txtPassword")
    user_email.send_keys("admin123")

    login_button = driver.find_element_by_css_selector("#btnLogin")
    login_button.submit()

    # driver.save_screenshot('screenshot.png')
finally:
    driver.quit()
