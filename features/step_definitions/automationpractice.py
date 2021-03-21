from pytest_bdd import scenarios, given, then, parsers, when
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

scenarios('', strict_gherkin=False)

@given("I am on Homepage")
def validate_homepage_url(init_driver):
    with allure.step("I am on Homepage"):
        if init_driver.current_url == "http://automationpractice.com/index.php":
            pass
        else:
            init_driver.get("http://automationpractice.com/index.php")

@given("I have a valid account")
def validate_valid_account(init_driver):
    with allure.step("I have a valid account"):
        if init_driver.current_url == "http://automationpractice.com/index.php?controller=authentication&back=my-account":
            pass
        else:
            init_driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

@when(parsers.parse('I click on "{string}" link'))
def click_on_link(init_driver, string):
    with allure.step(f'I click on "{string}" link'):
        init_driver.find_element_by_link_text(string).click()

@when(parsers.parse('I click over "{string}" button'))
def click_over_button(init_driver, string):
    with allure.step(f'I click over "{string}" button'):
        init_driver.find_element_by_id(string).click()

@then(parsers.parse('I am on "{string}" page'))
def validate_page(init_driver, string):
    with allure.step(f'I am on "{string}" page'):
        WebDriverWait(init_driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.page-heading')))
        elem=init_driver.find_element_by_css_selector('h1.page-heading')
        assert elem.get_attribute("textContent") == string

@then(parsers.parse('I validate "{string}" form is displayed'))
def validate_form_is_displayed(init_driver, string):
    with allure.step(f'I validate "{string}" form is displayed'):
        WebDriverWait(init_driver, 30).until(EC.presence_of_element_located((By.ID, string)))
        assert True == init_driver.find_element_by_id(string).is_displayed()

@then(parsers.parse('I validate "{string}" link is displayed'))
def validate_link_is_displayed(init_driver, string):
    with allure.step(f'I validate "{string}" link is displayed'):
        WebDriverWait(init_driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a//span[text()="' + string + '"]')))
        assert True == init_driver.find_element_by_xpath('//a//span[text()="' + string + '"]').is_displayed()

@then(parsers.parse('I check option "{string}" from Title'))
def _click(init_driver, string):
    with allure.step(f'I check option "{string}" from Title'):
        WebDriverWait(init_driver, 30).until(EC.presence_of_element_located((By.XPATH, '//label[contains(.,"' + string + '")]')))

@then(parsers.parse('I set "{ID}" input with "{string}" value'))
def _set_val(init_driver, ID, string):
    with allure.step(f'I set "{ID}" input with "{string}" value'):
        WebDriverWait(init_driver, 30).until(EC.presence_of_element_located((By.ID, ID)))
        init_driver.find_element_by_id(ID).clear()
        elem=init_driver.find_element_by_id(ID)
        assert '' == elem.get_attribute("value")
        elem.send_keys(string)
        assert string == elem.get_attribute("value")

@then(parsers.parse('I validate "{ID}" input contains "{string}" value'))
def _validate_val(init_driver, ID, string):
    with allure.step(f'I validate "{ID}" input contains "{string}" value'):
        elem = init_driver.find_element_by_id(ID)
        assert string == elem.get_attribute("value")

@then(parsers.parse('I click "{ID}" options and select "{pos}" position'))
def click_and_select(init_driver, ID, pos):
    with allure.step(f'I click "{ID}" options and select "{pos}" position'):
        elem = init_driver.find_element_by_id(ID)
        position = init_driver.find_element_by_xpath('//select[@id="' + ID + '"]/option[@value="' + pos + '"]')
        assert '0' == elem.get_attribute("selectedIndex")
        elem.click()
        init_driver.execute_script("arguments[0].scrollIntoView(true);",position)
        position.click()
        assert pos == elem.get_attribute("selectedIndex")

@then(parsers.parse('I click "{ID}" options and select "{value}" value'))
def click_on_option_and_select(init_driver,ID,value):
    with allure.step(f'I click "{ID}" options and select "{value}" value'):
        option=init_driver.find_element_by_id(ID)
        position = init_driver.find_element_by_xpath('//select[@id="' + ID + '"]/option[contains(text(),"' + value + '")]')
        assert  '0' == option.get_attribute("selectedIndex")
        option.click()
        init_driver.execute_script("arguments[0].scrollIntoView(true);", position)
        index=position.get_attribute("index")
        position.click()
        assert  index == option.get_attribute("selectedIndex")

@then(parsers.parse('I validate "{linkText}" user created'))
def validate_string(init_driver,linkText):
    with allure.step(f'I validate "{linkText}" user created'):
        init_driver.execute_script("arguments[0].scrollIntoView(true);", init_driver.find_element_by_link_text(linkText))
        assert True == init_driver.find_element_by_link_text(linkText).is_displayed()