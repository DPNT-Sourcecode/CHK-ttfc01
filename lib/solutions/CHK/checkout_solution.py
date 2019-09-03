# noinspection PyUnusedLocal
import string
from .basket import Basket

PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10,
          'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50,
          'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
          'Y': 20, 'Z': 21}
PROMO_MULTIPLE_ITEMS_CHEAPER = {'A': [(5, 200), (3, 130)],
                                'B': [(2, 45)],
                                'H': [(10, 80), (5, 45)],
                                'K': [(2, 120)],
                                'P': [(5, 200)],
                                'Q': [(3, 80)],
                                'V': [(3, 130), (2, 90)]}

PROMO_BUY_NX_GET_Y = {'E': [(2, 'B')],  # 2 items E gives item B for free],
                      'N': [(3, 'M')],
                      'R': [(3, 'Q')]}

PROMO_BUY_NX_GET_X = {'F': [(2, 'F')],
                      'U': [(3, 'U')]}

PROMOS = [PROMO_BUY_NX_GET_Y,
          PROMO_BUY_NX_GET_X,
          PROMO_MULTIPLE_ITEMS_CHEAPER,
          PROMO_BUY_NX_GET_X]  # promos applied in order


def checkout(skus):
    if len(set(list(skus)) - set(list(string.ascii_uppercase))) > 0:
        return -1
    basket = Basket(skus, PRICES, PROMOS)
    basket_value = basket.get_basket_total_value()

    return basket_value


