from selenium import webdriver


class Base:
    """This is Base Class for Selenium Project to getting started with."""
    browser = None

    def __init__(self):
        super(Base).__init__()
        self.browser = webdriver.Chrome(r"tr_selenium\driver\chromedriver.exe")

    def geturl(self,url):
        self.browser.get(url)
    def __del__(self):
        self.browser.close()