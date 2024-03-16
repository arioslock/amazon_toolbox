from flask import Blueprint, render_template, request
import json

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = request.form
    dict_from_form = form.to_dict(flat=False) 
    json_data = json.dumps(dict_from_form)

    return render_template("calculator.html")

