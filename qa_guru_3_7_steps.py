import allure
import pytest
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selenium.webdriver import Edge
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'Mimalen')
@allure.severity(Severity.NORMAL)
@allure.feature('Check the task')
@allure.story('Steps with allure.step')
@allure.link('https://github.com', name='Test_steps')
def test_github_issue():
    browser.config.driver = Edge()
    with allure.step('Open the main page'):
        browser.open('https://github.com/')
    with allure.step('Serch for the repository'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example')
        browser.element('.header-search-input').press_enter()
    with allure.step('Open the repository'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Open tab issues'):
        browser.element('#issues-tab').click()
    with allure.step('Checking issue number 76'):
        browser.element(by.partial_text('#76pip')).should(be.visible)

    browser.quit()
