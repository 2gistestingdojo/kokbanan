from base_test_case import BaseTestCase
import unittest


class Bug2Test(BaseTestCase):

    def test_bug1(self):
        main_window = self.driver.find_element_by_class_name('Window')

        search_button = main_window.find_element_by_name('Добавить')
        search_button.click()

        add_form = main_window.find_element_by_name('Add new product')
        textarea = add_form.find_elements_by_class_name('TextBox')
        textarea.send_keys('test')

        button = add_form.find_elements_by_class_name('TextBox')
        button.click()

        products_list = main_window.find_element_by_id('ListView')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        product_name = product_items.find_elements_by_name('test')

        self.assertFalse(product_name)

if __name__ == '__main__':
    unittest.main()
