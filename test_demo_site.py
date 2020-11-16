from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_demo_site(self):
        self.open("https://seleniumbase.io/demo_page.html")
        self.assert_title("Web Testing Page")
        self.assert_element("tbody#tbodyId")
        self.assert_text("Demo Page", "h1")
        self.type("#myTextInput", "This is Automated")
        self.type("textarea.area1", "Testing Time!\n")
        self.type('[name="preText2"]', "Typing Text!")
        self.assert_text("Automation Practice", "h3")
        self.hover_and_click("#myDropdown", "#dropOption2")
        self.assert_text("Link Two Selected", "h3")
        self.assert_text("This Text is Green", "#pText")
        self.click("#myButton")
        self.assert_text("This Text is Purple", "#pText")
        self.assert_element('svg[name="svgName"]')
        self.assert_element('progress[value="50"]')
        self.press_right_arrow("#myslider", times=5)
        self.assert_element('progress[value="100"]')
        self.assert_element('meter[value="0.25"]')
        self.select_option_by_text("#mySelect", "Set to 75%")
        self.assert_element('meter[value="0.75"]')
        self.assert_false(self.is_element_visible("img"))
        self.switch_to_frame("#myFrame1")
        self.assert_true(self.is_element_visible("img"))
        self.switch_to_default_content()
        self.assert_false(self.is_text_visible("iFrame Text"))
        self.switch_to_frame("#myFrame2")
        self.assert_true(self.is_text_visible("iFrame Text"))
        self.switch_to_default_content()
        self.assert_false(self.is_selected("#radioButton2"))
        self.click("#radioButton2")
        self.assert_true(self.is_selected("#radioButton2"))
        self.assert_false(self.is_selected("#checkBox1"))
        self.click("#checkBox1")
        self.assert_true(self.is_selected("#checkBox1"))
        self.assert_false(self.is_selected("#checkBox2"))
        self.assert_false(self.is_selected("#checkBox3"))
        self.assert_false(self.is_selected("#checkBox4"))
        self.click_visible_elements("input.checkBoxClassB")
        self.assert_true(self.is_selected("#checkBox2"))
        self.assert_true(self.is_selected("#checkBox3"))
        self.assert_true(self.is_selected("#checkBox4"))
        self.assert_false(self.is_element_visible(".fBox"))
        self.switch_to_frame("#myFrame3")
        self.assert_true(self.is_element_visible(".fBox"))
        self.assert_false(self.is_selected(".fBox"))
        self.click(".fBox")
        self.assert_true(self.is_selected(".fBox"))
        self.switch_to_default_content()
        self.assert_link_text("seleniumbase.com")
        self.assert_link_text("SeleniumBase on GitHub")
        self.assert_link_text("seleniumbase.io")
        self.click_link_text("SeleniumBase Demo Page")
        self.assert_exact_text("Demo Page", "h1")