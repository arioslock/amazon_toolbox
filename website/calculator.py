from flask import Blueprint, render_template, request
import json

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = request.form
    dict_from_form = form.to_dict(flat=False) 
    json_data = json.dumps(dict_from_form)
    print(json_data)
    # if request.method == 'POST':
    #     net_product_price = request.form.get('net_product_price')
    #     vat = request.form.get('vat')
    #     amazon_fee = request.form.get('amazon_fee')
    #     fixed_costs = request.form.get('fixed_costs')
    #     margin = request.form.get('margin')
    #     extra_perc_from_selling_price = request.form.get('extra_perc_from_selling_price')
    #     net_delivery_cost = request.form.get('net_delivery_cost')

    return render_template("calculator.html")

