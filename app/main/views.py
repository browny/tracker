# -*- coding: utf-8 -*-

import json
import controller
from functools import wraps
from flask import redirect, request, current_app, jsonify
from . import main


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs).data) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function


@main.route('/<stock_name>', methods=['GET'])
@support_jsonp
def parse(stock_name):

    response_dict = controller.query_by_string(stock_name)
    item_list = response_dict.get('items')

    # for item in item_list:
    #     snippet = item['snippet']
    #     get_date_from_snippet(snippet)

    return jsonify(items=item_list)

