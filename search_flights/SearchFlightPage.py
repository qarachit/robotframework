from Web import Web
import time

class SearchFlightPage(object):

    __url = "http://blazedemo.com/"

    def open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

    def select_departure_city(self, city):
        time.sleep(5)
        self._web.get_web_element_by_xpath("//select[@name='fromPort']/option[@value='{}']".format(city)).click()

    def select_destination_city(self, city):
        time.sleep(5)
        self._web.get_web_element_by_xpath("//select[@name='toPort']/option[@value='{}']".format(city)).click()

    def search_for_flights(self):
        time.sleep(5)
        self._web.get_web_element_by_xpath("//input[@type='submit']").click()

    def get_found_flights(self):
        time.sleep(5)
        return self._web.get_web_elements_by_xpath("//table[@class='table']/tbody/tr")

    def close(self):
        self._web.close_all()