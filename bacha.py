from seleniumbase import BaseCase
import selenium
from selenium.webdriver.support.ui import Select
from time import sleep


class MyTestClass(BaseCase):

    def test_basic(self):
        self.open("https://bachacoffeeuat.brayleinosplash.com/")
        self.maximize_window()
        sleep(10)
        self.assert_text('THE PERFECT BREW FOR', '.title-heading')

        self.is_element_visible('//a[@class="btn btn-orange medium"')

    def test_btn(self):
        self.open("https://bachacoffeeuat.brayleinosplash.com/")
        self.is_element_visible('//a[@class="btn btn-orange medium" and '
                                '@href="/Cart/ShoppingCart/AddToCart?sku=C9074&variant=C9074-001&addon=0&quantity=1" '
                                ']')

    def test_btn_next(self):
        self.open("https://bachacoffeeuat.brayleinosplash.com/")

        text1 = self.get_text('//div[@class="best-sellers__item bls-carousel__item active"]//div['
                              '@class="best-sellers__name"]')

        print(text1)
        self.click('//button[@class="bls-carousel__button bls-carousel__button--next"]')

        text2 = self.get_text('//div[@class="best-sellers__item bls-carousel__item active"]//div['
                              '@class="best-sellers__name"]')
        print(text2)
        assert text1 != text2, "Scroll not working !!!"

        sleep(5)

    def test_btn_prev(self):
        self.open("https://bachacoffeeuat.brayleinosplash.com/")
        self.click('//button[@class="bls-carousel__button bls-carousel__button--prev"]')
        sleep(5)

        all_items = self.find_elements('//div[@class="best-sellers__item bls-carousel__item"]//div['
                                       '@class="best-sellers__name"]')

        for i in all_items:
            print(list(all_items))

    # for i in len(all_items):

    # if text != array[i]

