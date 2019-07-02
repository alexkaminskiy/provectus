import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains



class TestRozetka(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome("C:\\Users\\notebook\\Desktop\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://rozetka.com.ua/")


    def test_menu(self):
        cities_link_xpath = "//div[@class='header-cities']/a"
        self.driver.find_element_by_xpath(cities_link_xpath).click()
        odessa_city_xpath = "//a[text()='Одесса ']"
        self.driver.find_element_by_xpath(odessa_city_xpath).click()

        search_bar_xpath = "//input[@name='search']"
        self.driver.find_element_by_xpath(search_bar_xpath).send_keys("Кондиционер\n")

        conditioner1_xpath = "//input[@value='001']/..//div[@class='g-i-tile-i-title clearfix']//a"
        self.driver.find_element_by_xpath(conditioner1_xpath).click()
        add_to_compare_cond1_xpath = "//a[@class='detail-comparison-link novisited ng-star-inserted']"
        add_to_compare_cond1_locator = self.driver.find_element_by_xpath(add_to_compare_cond1_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(add_to_compare_cond1_locator).click().perform()

        self.driver.back()

        conditioner2_xpath = "//input[@value='002']/..//div[@class='g-i-tile-i-title clearfix']//a"
        self.driver.find_element_by_xpath(conditioner2_xpath).click()
        add_to_compare_cond2_xpath = "//a[@class='detail-comparison-link novisited ng-star-inserted']"
        add_to_compare_cond2_locator = self.driver.find_element_by_xpath(add_to_compare_cond2_xpath)
        actions1 = ActionChains(self.driver)
        actions1.move_to_element(add_to_compare_cond2_locator).click().perform()

        comparison_xpath = "//a[@class='header-actions__button header-actions__button_type_compare header-actions__button-state-active whitelink ng-star-inserted']"
        self.driver.find_element_by_xpath(comparison_xpath).click()
        compare_btn_xpath = "//div[@class='btn-link-to-compare']/a"
        self.driver.find_element_by_xpath(compare_btn_xpath).click()

        list_of_web_elements = self.driver.find_elements_by_xpath("//div[@class='comparison-t-row' and @name='equal']/div")
        list_of_param = []
        for item in list_of_web_elements:
            list_of_param.append(item.text)
        print("Equal params are ")
        print(list_of_param)

    @classmethod
    def tearDownClass(self):
        self.driver.close()


    if __name__ == '__main__':
        unittest.main()
