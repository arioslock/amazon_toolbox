from typing import Final

class PricePayload:
    def __init__(self, PRODUCT_PRICE, VAT, AMZ_FEE, FIXED_COSTS, MARGIN, EXTRA_PERC_FROM_SELLING_PRICE, DELIVERY_COST) -> None:
        self.PRODUCT_PRICE: Final = PRODUCT_PRICE
        self.VAT: Final = VAT
        self.AMZ_FEE: Final = AMZ_FEE
        self.FIXED_COSTS: Final = FIXED_COSTS
        self.MARGIN: Final = MARGIN
        self.EXTRA_PERC_FROM_SELLING_PRICE: Final = EXTRA_PERC_FROM_SELLING_PRICE
        self.DELIVERY_COST: Final = DELIVERY_COST
