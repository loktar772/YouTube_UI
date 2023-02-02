from selenium.webdriver.support.events import AbstractEventListener

from base.seleniumbase import SeleniumBase


class MyListener(AbstractEventListener):

     def before_click(self, element, driver):#перед тем как нажать на любой элементб ыелениум будет->
        SeleniumBase(driver).delete_cookie('ak_bmsc')#удалит куки с этим именем который блокирует тест

     def after_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ak_bmsc')#после того как прошёл тест, селениум автоматом удаляет этот куки