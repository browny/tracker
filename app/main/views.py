# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, make_response
from flask import current_app
import controller
from .. import db
from . import main


@main.route('/<stock_name>', methods=['GET'])
def parse(stock_name):

    response_dict = controller.query_by_string(stock_name)
    item_list = response_dict.get('items')

    # for item in item_list:
    #     snippet = item['snippet']
    #     get_date_from_snippet(snippet)

    return jsonify(items=item_list)

