# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from base_test_case import BaseTestCase
import unittest


class Bug6Test(BaseTestCase):

    def test_bug6_change(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        product_item = main_window.find_element_by_name('Клавиатура Logitec')

        ActionChains(self.driver).move_to_element(product_item).double_click().perform()

        frame = self.driver.find_element_by_id('ChangeProductWindow')
        category = frame.find_element_by_id('CategoryCW')
        category.click()
        frame.find_element_by_name('Сетевое оборудование').click()

        frame.find_element_by_id('SaveCW').click()

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')

        flag = False
        for i in product_items:
            if i.find_element_by_class_name('TextBlock').get_attribute('Name') == 'Клавиатура Logitec':
                if i.find_element_by_class_name('TextBlock').get_attribute('Name') == 'Перефирия':
                    flag=True

        self.assertFalse(flag)

if __name__ == '__main__':
    unittest.main()
