

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

def checkout(skus):
    skus = skus.encode('utf-8')
    basket = dict((product, skus.count(product)) for product in list(skus))
    basket_value = 0
    for product in basket.items():
        single_price = PRICES[product[0]]
        

