import CalculatorService
import PricePayload


product_1 = PricePayload.PricePayload(product_price=100, vat=0.23, amz_fee=0.15, fixed_costs=10, margin=0.15, 
                             extra_perc_from_selling_price=0.2, net_delivery_cost=7)
calculator = CalculatorService.PriceCalculator

# Dostęp do atrybutów obiektu
print(vars(product_1))  

# amz_price_product_1 = calculator.calculate_price(product_price=product_1.product_price, )

