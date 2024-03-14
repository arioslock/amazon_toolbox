import PricePayload as pp

class PriceCalculator:
    """
    A class for calculating prices and performing price checks.

    Attributes:
        None

    Methods:
        calculate_price: Calculates the price for objects from the PricePayload class.
        check_price: Performs a check for calculated prices for objects from the PricePayload class.
    """


    def calculate_price (price_payload: pp.PricePayload):
        """
        Calculate the price for a product on Amazon based on variables of price_payload object.

        Args:
            price_payload (object): A price object from the PricePayload class.

        Returns:
            PricePayload object with calculated price.
        """

        net_price = ((price_payload.net_product_price * (1 + price_payload.margin)) + price_payload.fixed_costs + price_payload.net_delivery_cost) 
        perc_price_substraction = (price_payload.vat*(1/1/(1+price_payload.vat))) + price_payload.amz_fee + price_payload.extra_perc_from_selling_price
        calculated_price = net_price/(1-perc_price_substraction)

        price_payload.calculated_price = calculated_price
    
    def is_price_calculated_correctly (price_payload: pp.PricePayload):
        """
        This function takes a PricePayload object to calculate price components and checks if the difference between the net product price and the price check is in the range of (-0.1 to 0.1).

        Args:
            price_payload (object): A price object from the PricePayload class.

        Returns:
            PricePayload object with calculated variables representing price components. 
            If the calculated price is correct. The function prints the message "Price calculated correctly" if the price is correct. 
            If not, it prints the message "Price miscalculation" along with the net price and the difference between the price and the final price.
        """

        price_payload.calculated_vat = price_payload.calculated_price * (price_payload.vat*(1/1/(1+price_payload.vat)))
        price_payload.calculated_amz_fee = price_payload.calculated_price * price_payload.amz_fee
        price_payload.calculated_margin = price_payload.net_product_price * price_payload.margin
        price_payload.calculated_extra_perc_from_selling_price = price_payload.calculated_price * price_payload.extra_perc_from_selling_price
        price_payload.price_check = price_payload.calculated_price - price_payload.calculated_vat - price_payload.calculated_amz_fee - price_payload.fixed_costs - price_payload.calculated_margin - price_payload.calculated_extra_perc_from_selling_price - price_payload.net_delivery_cost

        price_payload.price_calculated_corretly = (-0.1 < (price_payload.net_product_price - price_payload.price_check) < 0.1)
        return price_payload.price_calculated_corretly
