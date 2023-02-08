import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selenium.webdriver import Edge
from selene.support.shared import browser


@allure.tag('web')
@allure.label('owner', 'Mimalen')
@allure.severity(Severity.NORMAL)
@allure.feature('Check the task')
@allure.story('Selene')
@allure.link('https://github.com', name='test')
def test_github_issue():
    browser.config.driver = Edge()
    browser.open('https://github.com/')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#76')).should(be.visible)

    browser.quit()