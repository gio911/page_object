from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)   

    def is_element_present(self, how, what):  #now we can use this method for cheking wether this element is present in this page or not
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False
        return True        