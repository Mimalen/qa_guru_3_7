import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selenium.webdriver import Edge
from selene.support.shared import browser
from allure import attachment_type


@allure.tag('web')
@allure.label('owner', 'Mimalen')
@allure.severity(Severity.NORMAL)
@allure.feature('Check the task')
@allure.story('Decorator')
@allure.link('https://github.com', name='test_decorator')
def test_decorator():
    browser.config.driver = Edge()
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    open_repository('eroshenkoam/allure-example')
    open_issue()
    check_repository('#76')


@allure.step('Open the main page')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Search for repository{repository}')
def search_repository(repository):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repository)
    browser.element('.header-search-input').press_enter()


@allure.step('Open repository {repository}')
def open_repository(repository):
    browser.element(by.link_text(repository)).click()


@allure.step('open tab issues')
def open_tab():
    browser.element('#issues-tab').click()


@allure.step('Checking issue number {num}')
def check_repository_number(num):
    browser.element(by.partial_text(num)).should(be.visible)
    allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot1", attachment_type=AttachmentType.PNG)
    s(by.partial_text(number)).click()

browser.quit()
