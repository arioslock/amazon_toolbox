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

    def calculate_price (product_price, vat, amz_fee, fixed_costs, margin, extra_perc_from_selling_price, net_delivery_cost) -> int:
        """
        Calculate the price for a product on Amazon based on given inputs.

        Args:
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

        net_price = ((product_price * (1 + margin)) + fixed_costs + net_delivery_cost) 
        magic_numebr = (vat*(1/1/(1+vat))) + amz_fee + extra_perc_from_selling_price
        final_price = net_price/(1-magic_numebr)

        return final_price
    
    def check_price (final_price, product_price, vat, amz_fee, fixed_costs, margin, extra_perc_from_selling_price, net_delivery_cost) -> int:
        """
        Based on the calculated price, count each component of price and extract them from the final price, checking if what's left is equal to the product price.

        Args:
            final_price (int): Price of product for Amazon.
            product_price (int): Net product price.
            vat (int): VAT value for the given product in the chosen country.
            amz_fee (int): Amazon fee taken from the sold product, based on the category of the product.
            fixed_costs (int): Fixed cost that the seller wants to add.
            margin (int): Percentage of net product price, earning of the seller.
            extra_perc_from_selling_price (int): Extra percentage added to the final price chosen by the seller.
            net_delivery_cost (int): If included in price, net value of delivering the product to the customer.

        Return:
            int: If the counted price is equal to the final price minus all price components, return final price and values for all counted price components. 
            If not, return product price and the difference between final price and all price components.
        """

        vat = final_price * (vat*(1/1/(1+vat)))
        amz_fee = final_price * amz_fee
        margin = product_price * margin
        extra_perc_from_selling_price = final_price * extra_perc_from_selling_price
        price_check = final_price - amz_fee - fixed_costs - extra_perc_from_selling_price - vat - margin - net_delivery_cost

        if price_check == product_price: 
            return final_price, product_price, vat, amz_fee, fixed_costs, margin, extra_perc_from_selling_price, net_delivery_cost
        else:
            print(f"price miss calculation. Diffrent beetwen final price and counted component = {price_check}")
            return product_price, price_check