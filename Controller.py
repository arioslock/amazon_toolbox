import json
import CalculatorService as cs
import PricePayload as pp


def calculate_price_for_web(price_components: json) -> object:
    
    data = json.loads(price_components)

    for key, value in data.items():
      data[key] = float(value[0])

    price_object = pp.PricePayload(**data)

    cs.PriceCalculator.calculate_price(price_object)

    if cs.PriceCalculator.is_price_calculated_correctly(price_object) == True:
      return price_object
    else:
       return print("price calculation error")
