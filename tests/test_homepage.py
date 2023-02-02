import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        #homepage_nav.driver.delete_cookie('ak_bmsc')
        #actual_links = homepage_nav.get_nav_links_text()
        #expected_links = homepage_nav.NAV_LINK_TEXT
        #assert expected_links == actual_links, 'Validating Nav Links text'
        #elements = homepage_nav.get_nav_links()
        #cookies = homepage_nav.driver.get_cookies() #через селениум метод получаем кукис
        #cookies_names = [cookie['name'] for cookie in cookies] #поиск куки по именам, через ключ НАМЕ ищем похожие имена куки
        #print(cookies)
        #print('----------------------')
        #print(cookies_names)
        #homepage_nav.driver.delete_all_cookies()
        #elements = homepage_nav.get_nav_links()
        #homepage_nav.get_nav_link_by_name('Home').click()
        for indx in range(8):
            homepage_nav.get_nav_links()[indx].click()
            #homepage_nav.driver.delete_cookie('ak_bmsc')
            #for cookie_name in cookies_names:
                #homepage_nav.driver.delete_cookie('ak_bmsc')
                #homepage_nav.driver.refresh()
                #homepage_nav.is_visible('tag_name', 'h1', cookie_name)

            #time.sleep(1.5)