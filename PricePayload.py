class PricePayload:
    def __init__(self, product_price, VAT, AMZ_fee, fixed_costs, margin, extra_perc_from_selling_price, delivery_cost) -> None:
        self.product_price = product_price
        self.VAT = VAT
        self.AMZ_fee = AMZ_fee
        self.fixed_costs = fixed_costs
        self.margin = margin
        self.extra_perc_from_selling_price = extra_perc_from_selling_price
        self.delivery_cost = delivery_cost
