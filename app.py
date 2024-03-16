import CalculatorService as cs
import PricePayload as pp


product_1 = pp.PricePayload(net_product_price=100, vat=0.23, amz_fee=0.15, fixed_costs=10, margin=0.15, 
                             extra_perc_from_selling_price=0.02, net_delivery_cost=7)
calculator = cs.PriceCalculator


print(vars(product_1))  

calculator.calculate_price(product_1)

print(vars(product_1))

print(calculator.is_price_calculated_correctly(product_1))

print(vars(product_1))
