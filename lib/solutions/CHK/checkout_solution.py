

# noinspection PyUnusedLocal
# skus = unicode string
import string
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
PROMO = {'A': (3, 130), 'B': (2, 45), 'A': (5, 200)}


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity






def calculate_product_price(p_name, p_quantity):
    if p_name in PROMO and p_quantity >= PROMO[p_name][0]:
        p_promo = PROMO[p_name]
        quant, price = p_promo
        return ((p_quantity // quant) * price) + (p_quantity % quant) * PRICES[p_name]
    else:
        return p_quantity * PRICES[p_name]



def checkout(skus):
    if len(set(list(skus)) - set(list(string.ascii_uppercase))) > 0:
        return -1
    basket = dict((product, skus.count(product)) for product in list(skus))
    basket_value = 0
    for product in basket.items():
        p_name, p_quantity = product[0], product[1]
        if not PRICES[p_name]:
            return -1
        basket_value += calculate_product_price(p_name, p_quantity)

    return basket_value



# ------ unit tests ------
import unittest

class TestCheckout(unittest.TestCase):

    def test_five_A_for_200(self):
        actual = checkout('AAAAA')
        expected = 200

    def test_three_A_for_130(self):
        actual = checkout('AAA')
        expected = 130

    def test_buy_two_E_get_B_free_with_two_B_for_lower_price(self):
        actual = checkout('EEBB')
        expected = 110
        self.assertEqual(expected, actual)

    def test_buy_two_E_get_B_free_with_no_B_in_basket(self):
        actual = checkout('EEA')
        expected = 130
        self.assertEqual(expected, actual)

    def test_buy_two_E_get_B_free_with_third_E_and_extra_B(self):
        actual = checkout('EEBEB')
        expected = 150
        self.assertEqual(expected, actual)

    def test_buy_two_E_get_B_free(self):
        actual = checkout('EEB')
        expected = 80
        self.assertEqual(expected, actual)

    def test_single_product(self):
        actual = checkout('C')
        expected = 20
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

