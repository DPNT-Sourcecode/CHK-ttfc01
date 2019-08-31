

# noinspection PyUnusedLocal
# skus = unicode string
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

def checkout(skus):
    skus = skus.encode('utf-8')
    basket = dict((product, skus.count(product)) for product in list(skus))




