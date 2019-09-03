import unittest
from .checkout_solution import Basket

TEST_PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10,
               'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50,
               'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
               'Y': 20, 'Z': 21}
TEST_PROMO_MULTIPLE_ITEMS_CHEAPER = {'A': [(5, 200), (3, 130)],
                                     'B': [(2, 45)],
                                     'H': [(10, 80), (5, 45)],
                                     'K': [(2, 150)],
                                     'P': [(5, 200)],
                                     'Q': [(3, 80)],
                                     'V': [(3, 130), (2, 90)]}

TEST_PROMO_BUY_NX_GET_Y = {'E': [(2, 'B')],  # 2 items E gives item B for free],
                           'N': [(3, 'M')],
                           'R': [(3, 'Q')]}

TEST_PROMO_BUY_NX_GET_X = {'F': [(2, 'F')],
                           'U': [(3, 'U')]}

TEST_PROMO_BUY_ANY_N_ITEMS_FOR_X = ['S', 'T', 'X', 'Y', 'Z']

TEST_PROMOS = [TEST_PROMO_BUY_NX_GET_Y,
               TEST_PROMO_BUY_NX_GET_X,
               TEST_PROMO_MULTIPLE_ITEMS_CHEAPER]  # promos applied in order


class TestBasket(unittest.TestCase):

    def test_empty_basket(self):
        basket = Basket('', TEST_PRICES)
        actual = len(basket.products.keys())
        expected_number_of_items_in_basket = 0
        self.assertEqual(expected_number_of_items_in_basket, actual)

    def test_basket_with_one_item(self):
        basket = Basket('A', TEST_PRICES)
        actual = len(basket.products.keys())
        expected_number_of_items_in_basket = 1
        self.assertEqual(expected_number_of_items_in_basket, actual)

    def test_calculate_base_product_price(self):
        basket = Basket('', TEST_PRICES)
        actual = basket._calculate_base_product_price('A', 2)
        expected = 100
        self.assertEqual(expected, actual)

    def test_calc_buy_any_n_products_for_x(self):
        cases = [
            ('ZZZ', 45),
            ('SSS TTT XXX', 135),
            ('ZZZ XXX', 96),
            ('ZZZ ZYX XX', 124),
            ('XXY ZZ', 79),
            ('ZZ', 0),
            ('Z', 0),
            ('XXX', 45),
            ('SSSS', 65),
            ('TTTT', 65)]
        for case in cases:
            skus, expected = case[0].replace(' ', ''), case[1]
            basket = Basket(skus, TEST_PRICES)

            actual = basket.calc_buy_any_n_products_for_x(TEST_PROMO_BUY_ANY_N_ITEMS_FOR_X)

            self.assertEqual(expected, actual, 'Failing case: {}'.format(case[0]))

    def test_get_basket_total_value(self):
        cases = [('AAAAA PPPPP UUUU EE B RRR Q AAA HHHHHHHHHH VVV BB NNN M FFF KK QQQ VV HHHHH', 1640),
            ('FF', 20),
            ('AAAAA AAAAA', 400),
            ('AAAAA AAAAA AAAAA A ', 650),
            ('AAAAA AAAAA AAAAA AAA A ', 780),
            ('BB EE', 110),
            ('EE B EE', 160),
            ('EE BB EE', 160),
            ('EE BB', 110),
            ('EE B E B', 150),
            ('B EEE B ', 150),
            ('EE A', 130),
            ('EE B', 80),
            ('C', 20),
            ('', 0),
            ('EE', 80),
            ('AAA', 130),
            ('AAAAA', 200),
            ('BB', 45),
            ('BB AAAAA AAA A EE', 490),
            ('A BB A EE', 210),
            ('ABCDE', 155),
            ('AAA BBB C DD EEE A', 395),
            ('FF', 20),
            ('FF F', 20),
            ('FF FF', 30),
            ('FF FF F', 40),
            ('FF FF FF', 40),
            ('FF FF FF F', 50),
            ('FF FE ED BB B', 160),
            ('FFABCDECBAABCABBAAAEEAAFF', 695),
            ('AAAAAEEBAAABBFFF', 475),
            ('CDFFAECBDEAB', 300),
            (5 * 'H' + 10 * 'H', 125),
            (5 * 'H' + 21 * 'H', 215),
            (19 * 'H', 165),
            (20 * 'H', 160),
            ('NNN MM X BB', 270),
            ('QQQ', 80),
            ('RRR QQ', 180),
            ('UUU U', 120),
            ('UUU UU', 160),
            ('UUU UUU UU', 240),
            ('EE B RRR Q  VVV BB', 405),
            ('NNN M FFF KK QQQ VV', 460),
            (' EE B RRR Q  VVV BB NNN M FFF KK QQQ VV ', 865),
            ('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ', 1880),
            ('LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH', 1880),
            ('PPPPQRUVPQRUVPQRUVSU', 740),
            ('AAAAA PPPPP UUUU EE B RRR Q AAA HHHHHHHHHH VVV BB NNN M FFF KK QQQ VV HHHHH', 1640),
            ('UUUU FFF', 140)]
        for case in cases:
            skus, expected = case[0].replace(' ', ''), case[1]
            basket = Basket(skus, TEST_PRICES, TEST_PROMOS)

            actual = basket.get_basket_total_value()

            self.assertEqual(expected, actual, 'Failing case: {}'.format(case[0]))

    def test_check_if_valid_basket_with_invalid_products(self):
        basket = Basket('/?@', TEST_PRICES)
        actual = basket._check_if_valid_basket()
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_valid_basket_with_valid_products(self):
        basket = Basket('ABCD', TEST_PRICES)
        actual = basket._check_if_valid_basket()
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_valid_basket_with_valid_and_invalid_products(self):
        basket = Basket('ABZ?@CDXY', TEST_PRICES)
        actual = basket._check_if_valid_basket()
        expected = False
        self.assertEqual(expected, actual)

    def test_calc_buy_nx_get_x_free(self):
        cases = [
                 ('F', 10),
                 ('FF', 20),
                 ('FF F', 20),
                 ('FF FF', 30),
                 ('FF FF F', 40),
                 ('FF FF FF', 40),
                 ('FF FF FF F', 50),
                 ('UU', 80),
                 ('UUU', 120),
                 ('UUU U', 120),
                 ('UUU UU', 160),
                 ('UUU UUU UU', 240)]
        for case in cases:
            skus, expected = case[0].replace(' ', ''), case[1]
            basket = Basket(skus, TEST_PRICES)

            actual = basket.calc_buy_nx_get_x_free(TEST_PROMO_BUY_NX_GET_X)

            self.assertEqual(expected, actual, 'Failing case: {}'.format(case[0]))

    def test_calc_buy_nx_get_y_free(self):
        cases = [('EE B', 0),
                 ('EE BB', 1),
                 ('EEEE BB', 0),
                 ('EEEE BBB', 1),
                 ('EEEE BBB BBB', 4)]
        for case in cases:
            skus, expected = case[0].replace(' ', ''), case[1]
            basket = Basket(skus, TEST_PRICES)

            basket.calc_buy_nx_get_y_free(TEST_PROMO_BUY_NX_GET_Y)

            actual = basket.products['B']
            self.assertEqual(expected, actual, 'Failing case: {}'.format(case[0]))

    def test_calc_buy_nx_get_y_free_no_free_product_in_basket(self):
        test_promo = {'E': [(2, 'B')]}
        basket = Basket('EEEE', TEST_PRICES)

        basket.calc_buy_nx_get_y_free(test_promo)

        actual = 'B' not in basket.products.keys()
        expected = True
        self.assertEqual(expected, actual)

    def test_calc_buy_multiple_items_cheaper(self):
        cases = [('AA A', 130),
                 ('AA KK', 150),
                 ('VVV KK', 280),
                 ('AA', 0),
                 ('VVV VVV VVV', 390)]
        for case in cases:
            skus, expected = case[0].replace(' ', ''), case[1]
            basket = Basket(skus, TEST_PRICES)

            actual = basket.calc_buy_multiple_items_cheaper(TEST_PROMO_MULTIPLE_ITEMS_CHEAPER)

            self.assertEqual(expected, actual, 'Failing case: {}'.format(case[0]))

    def test_calc_buy_multiple_items_cheaper_applies_offer_for_higher_quantity_option_first(self):
        test_promo = {'V': [(2, 90), (3, 130)]}
        cases = [('VV', 90),
                 ('VVVV', 130),
                 ('VVV VVV VVV', 390)]
        for case in cases:
            skus, expected = case[0].replace(' ', ''), case[1]
            basket = Basket(skus, TEST_PRICES)

            actual = basket.calc_buy_multiple_items_cheaper(test_promo)

            self.assertEqual(expected, actual, 'Failing case: {}'.format(case[0]))


if __name__ == '__main__':
    unittest.main()
