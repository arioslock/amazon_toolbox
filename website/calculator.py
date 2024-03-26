from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import json
import Controller

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/calculator', methods=['GET', 'POST'])
@login_required
def calculator():
    if request.method == 'POST':
        form = request.form
        dict_from_form = form.to_dict(flat=False) 
        json_data = json.dumps(dict_from_form)
        product = Controller.calculate_price_for_web(json_data)
        print(vars(product))

    return render_template("calculator.html", user=current_user)

