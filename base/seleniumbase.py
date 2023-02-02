from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By  #
from selenium.webdriver.support import expected_conditions as ec  # слово as(как) разрешает сокращать или переименовывать фукцию
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:

    def __init__(self, driver):  # инициализация вебдрайвера
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def __get_selenium_by(self, find_by: str) -> dict:  # функция аргументов выдаёт тип данных стр и иницилизирует в строку
        find_by = find_by.lower()  # позволяет написание слов с большой буквы и ищет их
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'name': By.NAME,
                    'tag_name': By.TAG_NAME}  # инплементируем с помощью словаря,прописываем всё что доступно
        return locating[find_by]  # возврат словаря с условием что в нём есть ключ [find_by]

    # Эта функция будет возвращать ВебЭлемент который будет работать на is_visible,чтоб виден был на стр используем find_by,
    # используем селениум и локаторы. выбераем язык
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)  # для поиска элемента

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)  # если нет элементов

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)  # для поиска несколких элементов

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)  # если много элементов на странице

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]: #принимаем список состоящий из вебэлементов и возвращаем список из строк
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement: #запрашиваем из листа элементов один по названию и выводим в строке
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def delete_cookie(self, cookie_name: str) -> None:
        self.driver.delete_cookie(cookie_name)