from seleniumbase import BaseCase
import selenium
from selenium.webdriver.support.ui import Select
from time import sleep


class SendMail(BaseCase):

    def test_basic(self):
        self.open("https://www.crodapersonalcare.cn/zh-cn/register")
        self.maximize_window()
        sleep(1)
        self.send_keys('//input[@class="form-control text-box single-line" and @id="Name"]', "test1")
        self.send_keys('//input[@class="form-control text-box single-line" and @id="Email"]', "ochuong@yopmail.com")
        self.click('//button[@class="btn btn-default" and @id="btn-verify-email"]', delay=2)
        sleep(60)
        self.click('//button[@class="btn btn-default" and @id="btn-verify-email"]', delay=2)
        sleep(60)
        self.click('//button[@class="btn btn-default" and @id="btn-verify-email"]', delay=2)
        sleep(60)
        self.click('//button[@class="btn btn-default" and @id="btn-verify-email"]', delay=2)
        sleep(60)
        self.click('//button[@class="btn btn-default" and @id="btn-verify-email"]', delay=2)
        sleep(60)
        self.click('//button[@class="btn btn-default" and @id="btn-verify-email"]', delay=2)
        sleep(60)
        self.save_screenshot()




