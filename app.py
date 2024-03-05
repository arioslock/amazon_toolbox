import CalculatorService as cs
import PricePayload as pp


product_1 = pp.PricePayload(net_product_price=100, vat=0.23, amz_fee=0.15, fixed_costs=10, margin=0.15, 
                             extra_perc_from_selling_price=0.02, net_delivery_cost=7)
calculator = cs.PriceCalculator

# Dostęp do atrybutów obiektu
print(vars(product_1))  

product_1.calculated_price = calculator.calculate_price(product_1)

print(product_1.calculated_price)

product_1_price_check = calculator.check_price(product_1)

print(vars(product_1_price_check)) 

