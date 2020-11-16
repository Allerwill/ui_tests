from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


class MyTestClass(BaseCase):

    # Next button -> end of list items
    def test_btn_next(self):
        self.open("https://blsvnint.brayleinosplash.com/")
        self.maximize_window()
        sleep(3)

        elements = self.find_elements(
            '//div[@class="bls-select"]//select[@class="btn-select--white invisible"]//option')

        print("Total elements: ", len(elements))
        print(list(elements))

        print(len(elements))
        for i in range(len(elements) - 2):
            self.click('//a[@class="btn btn-ico btn-next"]', delay=2)
        sleep(3)

    # Checking if direct to case studies page when step back to All Expertise at the first
    def test_btn_prev_at_first(self):
        self.open("https://blsvnint.brayleinosplash.com/")
        self.maximize_window()
        sleep(3)
        self.click('//a[@class="btn btn-ico btn-prev"]', delay=2)
        self.get_link_status_code('link:/work.html', True, 2)

    # Checking if each case study content is visible
    def test_case_study_contents(self):
        self.open("https://blsvnint.brayleinosplash.com/")
        self.maximize_window()
        sleep(3)

        elements = self.find_elements(
            '//div[@class="bls-select"]//select[@class="btn-select--white invisible"]//option')

        print("Total elements: ", len(elements))
        print(list(elements))

        print(len(elements))
        for i in range(len(elements) - 2):
            self.click('//a[@class="btn btn-ico btn-next"]', delay=2)
            self.is_element_visible('//div[@id="divCaseStudyDescription"]//div[@class="desc"]//p')
            self.is_element_visible('//div[@class="case-studies-slide__wrapper"]//div[@class="img"]')
            self.is_element_visible('//div[@class="case-studies-slide__wrapper"]//div[@class="img"]//span['
                                    '@class="text-left"]')
            self.is_element_visible('//div[@class="case-studies-slide__wrapper"]//div[@class="desc"]')
            # div#divCaseStudySlide a
            link_cs = self.get_attribute('//div[@class="case-studies-slide__wrapper"]//a[@class="btn btn-secondary"]',
                                         'href')
            print(link_cs)

            self.get_link_status_code(link_cs)

            self.get_link_status_code('https://blsvnint.brayleinosplash.com/work/volvo-c30-digital'
                                      '-launch-campaign.html')
            self.get_link_status_code('https://blsvnint.brayleinosplash.com/work.html')

            # Checking is slider is available if the slider item >1
            is_slider_visible = self.is_element_visible('//div[@class="bls-carousel"]//div['
                                                        '@class="bls-carousel__dots"]//button['
                                                        '@class="bls-carousel__dot"]')
            if is_slider_visible != '':
                slider_items_arr = self.find_elements(
                    '//div[@class="case-studies-slide__wrapper"]//div[@class="bls-carousel"]//div['
                    '@class="bls-carousel__dots"]')
                print("List dots", list(slider_items_arr))
                print("Total dots: ", len(slider_items_arr))

                for j in range(len(slider_items_arr)):
                    self.is_element_visible('//li[@class="bls-carousel__item active in-view"]//div[@class="img"]')
                    self.is_element_visible('//li[@class="bls-carousel__item active in-view"]//figcaption//span['
                                            '@class="text-left"]')
                    self.is_element_visible('//li[@class="bls-carousel__item active in-view"]//div[@class="desc"]')
                    self.click('//div[@class="case-studies-slide__wrapper"]//div[@class="bls-carousel__nav"]//button['
                               '@class="bls-carousel__button bls-carousel__button--next"]')
                    sleep(3)
                    break

            sleep(3)