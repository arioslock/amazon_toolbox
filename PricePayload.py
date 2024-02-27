from typing import Final

class PricePayload:
    """
    This class represents product price and contains all elements that can be included in the price.

    Attributes:
        product_price (int): Net product price.
        vat (int): Value of VAT for a given product in a given country.
        amz_fee (int): Value of Amazon fee depending on product category and country.
        fixed_costs (int): Net fixed costs that the seller needs to cover.
        margin (int): Margin that will be calculated based on the net product price.
        extra_perc_from_selling_price (int): Extra percentage added to the selling price if needed.
        net_delivery_cost (int): Cost of delivering the product to the customer if hidden in price.
    """
    def __init__(self, product_price: int, vat: int, amz_fee: int, fixed_costs: int, margin: int, 
                 extra_perc_from_selling_price: int, net_delivery_cost: int) -> None:
        self.product_price: Final = product_price
        self.vat: Final = vat
        self.amz_fee: Final = amz_fee
        self.fixed_costs: Final = fixed_costs
        self.margin: Final = margin
        self.extra_perc_from_selling_price: Final = extra_perc_from_selling_price
        self.net_delivery_cost: Final = net_delivery_cost
