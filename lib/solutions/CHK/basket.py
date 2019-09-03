class Basket:

    def __init__(self, skus, prices, promos=None):
        self.skus = skus
        self.prices = prices
        self.promos = promos
        self.products = dict((product, skus.count(product)) for product in list(skus))

    def get_basket_total_value(self):
        if not self._check_if_valid_basket():
            return -1
        basket_value = 0
        self.calc_buy_nx_get_y_free(self.promos[0])
        basket_value += self.calc_buy_nx_get_x_free(self.promos[1])
        basket_value += self.calc_buy_multiple_items_cheaper(self.promos[2])

        for product in self.products.items():
            p_name, p_quantity = product[0], product[1]
            basket_value += self._calculate_base_product_price(p_name, p_quantity)

        return basket_value

    def _calculate_base_product_price(self, p_name, p_quantity):
        return p_quantity * self.prices[p_name]

    def _check_if_valid_basket(self):
        return all(product in self.prices.keys() for product in self.products.keys())

    def calc_buy_any_n_products_for_x(self, offer_prods):
        """
        offer_prods - dict of products for which this offer can be applied
        """
        items_value = 0
        promo_items_prices_keys = set(offer_prods) & self.prices.keys()
        promo_items_dict = {p: self.prices[p] for p in promo_items_prices_keys}
        promo_items_prices = sorted(promo_items_dict.items(), key=lambda i: i[1], reverse=True)

        promo_items_from_basket_keys = set(offer_prods) & self.products.keys()
        promo_items_from_basket = {p: self.products[p] for p in promo_items_from_basket_keys}

        while sum([p[1] for p in promo_items_from_basket.items()]) >= 3:
            offer_applied_cntr = 3
            for o_product in promo_items_prices:
                op_name, op_price = o_product[0], o_product[1]
                if op_name in promo_items_from_basket:
                    while promo_items_from_basket[op_name] > 0 and offer_applied_cntr > 0:
                        promo_items_from_basket[op_name] -= 1
                        offer_applied_cntr -= 1

            if offer_applied_cntr == 0:
                items_value += 45

        for item in promo_items_from_basket.items():
            p_name, p_quantity = item[0], item[1]
            self.products[p_name] = p_quantity

        return items_value

    def calc_buy_nx_get_y_free(self, offer_prods):
        """
        offer_prods - dict of products for which this offer can be applied
        """
        for o_product in offer_prods.items():
            op_name, op_rule = o_product[0], o_product[1]
            quant_required, free_item = op_rule[0][0], op_rule[0][1]
            if op_name in self.products and self.products[op_name] >= quant_required and free_item in self.products:
                free_items = self.products[op_name] // quant_required
                while free_items > 0 and self.products[free_item] > 0:
                    self.products[free_item] -= 1
                    free_items -= 1

    def calc_buy_nx_get_x_free(self, offer_prods):
        """
        offer_prods - dict of products for which this offer can be applied
        """
        items_value = 0
        for o_product in offer_prods.items():
            op_name, op_rule = o_product[0], o_product[1]
            quant_required = op_rule[0][0]
            if op_name in self.products.keys():
                quantity = self.products[op_name]
                single_price = self.prices[op_name]
                if quant_required == 2:

                    if quantity == 1:
                        self.products[op_name] = 0
                        items_value += 1 * single_price
                    elif quantity == 3:
                        self.products[op_name] = 0
                        items_value += 2 * single_price
                    else:
                        self.products[op_name] = 0
                        items_value += single_price * (quantity - (quantity // 2 - 1))
                else:
                    if quantity <= 3:
                        self.products[op_name] = 0
                        items_value += single_price * quantity
                    else:
                        self.products[op_name] = 0
                        items_value += single_price * (quantity - (quantity // 3))

        return items_value

    def calc_buy_multiple_items_cheaper(self, offer_prods):
        """
        offer_prods - dict of products for which this offer can be applied
        """
        items_value = 0
        for product in self.products.items():
            p_name, p_quantity = product[0], product[1]
            if p_name in offer_prods:
                ordered_promos = sorted(offer_prods[p_name], key=lambda p: p[0], reverse=True)
                promo_price = 0
                lowest_promo_quantity = ordered_promos[-1][0]
                while p_quantity >= lowest_promo_quantity:
                    for promo in ordered_promos:
                        p_quant, p_value = promo[0], promo[1]
                        while p_quantity >= p_quant:
                            promo_price += p_value
                            p_quantity -= p_quant
                            self.products[p_name] -= p_quant

                items_value += promo_price
        return items_value

