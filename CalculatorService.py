import PricePayload as pp

class PriceCalculator:
    """
    A class for calculating prices and performing price checks.

    This class provides functions to calculate prices based on various factors 
    and to perform checks on prices for validity or comparison purposes.

    Attributes:
        None

    Methods:
        calculate_price: Calculates the price based on given inputs.
        check_price: Performs a check on a given price for validity or comparison.
    """

    def calculate_price (price_payload: pp.PricePayload) -> int:
        """
        Calculate the price for a product on Amazon based on variables of price_payload object.

        Args:
            price_payload (object): price object that include all components of price such as:
                product_price (int): Net product price.
                vat (int): VAT value for the given product in the chosen country.
                amz_fee (int): Amazon fee taken from the sold product, based on the category of the product.
                fixed_costs (int): Fixed cost that the seller wants to add.
                margin (int): Percentage of net product price, earning of the seller.
                extra_perc_from_selling_price (int): Extra percentage added to the final price chosen by the seller.
                net_delivery_cost (int): If included in price, net value of delivering the product to the customer.

        Returns:
            int: Calculated price for the product on Amazon.
        """

        net_price = ((price_payload.net_product_price * (1 + price_payload.margin)) + price_payload.fixed_costs + price_payload.net_delivery_cost) 
        magic_numebr = (price_payload.vat*(1/1/(1+price_payload.vat))) + price_payload.amz_fee + price_payload.extra_perc_from_selling_price
        calculated_price = net_price/(1-magic_numebr)

        return calculated_price
    
    def check_price (price_payload: pp.PricePayload) -> object:
        """
        Based on the calculated price, count each component of price and extract them from the final price, checking if what's left is equal to the product price.

        Args:
            price_payload (object): price object that include all components of price such as:
                final_price (int): calculated price.
                product_price (int): Net product price.
                vat (int): VAT value for the given product in the chosen country.
                amz_fee (int): Amazon fee taken from the sold product, based on the category of the product.
                fixed_costs (int): Fixed cost that the seller wants to add.
                margin (int): Percentage of net product price, earning of the seller.
                extra_perc_from_selling_price (int): Extra percentage added to the final price chosen by the seller.
                net_delivery_cost (int): If included in price, net value of delivering the product to the customer.

        Return:
            object: If the counted price is equal to the final price minus all price components, return object with all price component. 
            If not, return object with all price component and message with diffrence bettwen price and final price.
        """

        vat = price_payload.calculated_price * (price_payload.vat*(1/1/(1+price_payload.vat)))
        price_payload.calculated_vat = price_payload.calculated_price * (price_payload.vat*(1/1/(1+price_payload.vat)))
        print(f""" VAT
            vat:{vat}
            price_payload.calculated_vat :{price_payload.calculated_vat}
                """)
        amz_fee = price_payload.calculated_price * price_payload.amz_fee
        price_payload.calculated_amz_fee = price_payload.calculated_price * price_payload.amz_fee
        print(f""" amz_fee
            amz_fee:{amz_fee}
            pprice_payload.calculated_amz_fee :{price_payload.calculated_amz_fee}
                """)        
        margin = price_payload.net_product_price * price_payload.margin
        price_payload.calculated_margin = price_payload.net_product_price * price_payload.margin
        print(f""" margin
            margin:{margin}
            price_payload.calculated_margin :{price_payload.calculated_margin}
                """)  
        extra_perc_from_selling_price = price_payload.calculated_price * price_payload.extra_perc_from_selling_price
        price_payload.calculated_extra_perc_from_selling_price = price_payload.calculated_price * price_payload.extra_perc_from_selling_price
        print(f""" extra_perc_from_selling_price
            extra_perc_from_selling_price:{extra_perc_from_selling_price}
            price_payload.calculated_extra_perc_from_selling_price :{price_payload.calculated_extra_perc_from_selling_price}
                """)  
        price_check = price_payload.calculated_price - amz_fee - price_payload.fixed_costs - extra_perc_from_selling_price - vat - margin - price_payload.net_delivery_cost
        price_payload.price_check = price_payload.calculated_price - price_payload.calculated_vat - price_payload.calculated_amz_fee - price_payload.fixed_costs - price_payload.calculated_margin - price_payload.calculated_extra_perc_from_selling_price - price_payload.net_delivery_cost
        price_components = pp.PricePayload(net_product_price=price_check, vat=vat, amz_fee=amz_fee, fixed_costs=price_payload.fixed_costs, 
                                          margin=margin, extra_perc_from_selling_price=extra_perc_from_selling_price, net_delivery_cost=price_payload.net_delivery_cost)
        print(price_payload.calculated_price)
        print(price_check)
        print(price_payload.price_check)

        if -0.1 < (price_payload.net_product_price - price_payload.price_check) < 0.1: 
            print("Price calculated correctly")
            return price_components
        else:
            print(f"""Price miss calculation.
                  net price = {price_payload.net_product_price} 
                  price check = {price_check}""")
            return price_components