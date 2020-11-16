
import selenium
from selenium.webdriver.support.ui import Select
from seleniumbase import BaseCase
from time import sleep


class CaseStudies(BaseCase):
    def TestCaseStudies(self):
        self.open('https://blsvnint.brayleinosplash.com/')
        sleep(3)
        self.click('//a[@class="btn btn-ico btn-next"]')
        sleep(3)
        self.click('//a[@class="btn btn-ico btn-next"')
        sleep(3)
