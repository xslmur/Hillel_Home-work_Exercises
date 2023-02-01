# re-implementation for tests for Selenium IDE using WebDriver
# https://github.com/xslmur/Hillel_Home-work_Exercises/blob/main/HW26/test_hillel_selenium.side

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

ELEMENT_WAITING_TIMEOUT = 5

##########
# helpers
##########

def has_element_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False

def wait_for_element_by_xpath(driver, xpath):
    return WebDriverWait(driver, ELEMENT_WAITING_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, xpath)))

def open_page_and_login(driver, config):
    driver.get("https://" + config['auth']['basic']['user'] + ":" + config['auth']['basic']['pass'] + "@" + "qauto2.forstudy.space/")

    wait_for_element_by_xpath(driver, "//button[contains(text(), 'Sign In')]").click()

    input_email = driver.find_element(By.XPATH, "//input[@id='signinEmail']")
    input_email.send_keys(config['auth']['signin']['user'])

    input_pass = driver.find_element(By.XPATH, "//input[@id='signinPassword']")
    input_pass.send_keys(config['auth']['signin']['pass'])

    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

########
# tests
########

def test_garage_is_empty(driver, config):
    open_page_and_login(driver, config)
    assert(not has_element_by_xpath(driver, '//*[contains(@class, "car-list")]'))

def test_add_car_button_is_present(driver, config):
    open_page_and_login(driver, config)
    wait_for_element_by_xpath(driver, "//app-garage")
    assert(has_element_by_xpath(driver, "//button[contains(.,'Add car')]"))

def test_add_button_is_disabled(driver, config):
    open_page_and_login(driver, config)
    wait_for_element_by_xpath(driver, "//app-garage")
    driver.find_element(By.XPATH, "//button[contains(.,'Add car')]").click()
    assert(has_element_by_xpath(driver, "//button[text()='Add']"))
    assert(has_element_by_xpath(driver, "//button[text()='Add'][@disabled]"))

def test_add_button_is_enabled(driver, config):
    open_page_and_login(driver, config)
    wait_for_element_by_xpath(driver, "//app-garage")
    driver.find_element(By.XPATH, "//button[contains(.,'Add car')]").click()
    assert(has_element_by_xpath(driver, "//button[text()='Add']"))

    #fill mileage field
    driver.find_element(By.XPATH, "//input[@id='addCarMileage']").send_keys('20000')

    assert(not has_element_by_xpath(driver, "//button[text()='Add'][@disabled]"))

def test_add_car_check_in_garage_then_remove(driver, config):
    open_page_and_login(driver, config)
    wait_for_element_by_xpath(driver, "//app-garage")

    #add car
    driver.find_element(By.XPATH, "//button[contains(.,'Add car')]").click()
    driver.find_element(By.XPATH, "//input[@id='addCarMileage']").send_keys('20000')
    driver.find_element(By.XPATH, "//button[text()='Add']").click()

    #check car presence in the garage
    assert(wait_for_element_by_xpath(driver, "//li[@class='car-item']"))

    #remove car
    driver.find_element(By.XPATH, '//*[contains(@class, "btn-edit")]').click()
    driver.find_element(By.XPATH, "//button[text()='Remove car']").click()
    driver.find_element(By.XPATH, "//button[text()='Remove']").click()