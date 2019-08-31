

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
PROMO = {'A': (3, 130), 'B': (2, 45)}



def calculate_product_price(p_name, p_price):



def checkout(skus):
    skus = skus.encode('utf-8')
    basket = dict((product, skus.count(product)) for product in list(skus))
    basket_value = 0
    for product in basket.items():
        single_price = PRICES[product[0]]



