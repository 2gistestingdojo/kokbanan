# -*- coding: utf-8 -*-
from base_test_case import BaseTestCase
import unittest


class Bug5Test(BaseTestCase):

    def test_bug5_changeid(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        product_item = main_window.find_element_by_name('Телефон C1sko')
        self.driver.execute_script("input: ctrl_click", product_item)

        product_item = main_window.find_element_by_name('Клавиатура Logitec')
        self.driver.execute_script("input: ctrl_click", product_item)

        button = main_window.find_element_by_id('DeleteSelectedMW')
        button.click()

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        flag = False
        for i in product_items:
            if i.find_element_by_class_name('TextBlock').get_attribute('Name') == 'Клавиатура Logitec':
                flag=True

        self.assertFalse(flag)

if __name__ == '__main__':
    unittest.main()
