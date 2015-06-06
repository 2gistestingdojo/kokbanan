from base_test_case import BaseTestCase
import unittest


class ExampleTest(BaseTestCase):
    def test_example(self):
        main_window = self.driver.find_element_by_class_name('Window')

        search_string = main_window.find_element_by_class_name('TextBox')
        search_string.send_keys('Son')

        search_button = main_window.find_element_by_class_name('Button')
        search_button.click()

        products_list = main_window.find_element_by_id('ListView')
        product_items = products_list.find_elements_by_class_name('ListViewItem')

        self.assertEqual(len(product_items), 3)

if __name__ == '__main__':
    unittest.main()
