# декораторы (фикстуры) помогает сетапится -
# создавать драйверы в наших тестах, в наших других классах
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from abstract.selenium_listener import MyListener


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') #--headless  Запуск в автономном режиме, т. е. без зависимостей пользовательского интерфейса или сервера отображения.
    options.add_argument('--start-maximized') #Запускает браузер в развернутом виде, независимо от любых предыдущих настроек
    options.add_argument('--window-size=1200,850') #Устанавливает начальный размер окна. Предоставляется в виде строки в формате "800 600"
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):#ищем драйвер в папке куда положили
    options = get_chrome_options
    driver = webdriver.Chrome(options=options) #opti1-Aргумент,опти2-Переменная, пишем путь к папке драйвера
    return driver


@pytest.fixture(scope='function')#scope=(функция работы с браузером)если исп. фикстуру setup при ('function') каждый тест будет запускаться отдельно
def setup(request, get_webdriver):
    driver = get_webdriver# после сетапа запрашиваем драйвер
    driver = EventFiringWebDriver(driver, MyListener())#Затем перезаписываем. ипользуем листнер где на каждый клик работает удаление куки
    url = 'https://www.macys.com/'
    if request.cls is not None: #будет ли этот класс и есть ли этот класс
        request.cls.driver = driver
    driver.get(url) #метод get откроет url!
    driver.delete_all_cookies() # удаляет куки чтоб обходить защиту сайта и ходить по ссылкам
    yield driver #возврат драйвера
    driver.quit() #driver.close после окончания теста закроет окно браузера, quite - закроет браузер
