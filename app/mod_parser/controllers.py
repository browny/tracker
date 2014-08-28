# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, request, jsonify, make_response
import requests, json, re

# Define the blueprint: 'parser', set its url prefix: app.url/parser
mod_parser = Blueprint('parser', __name__, url_prefix='/parser')

QUERY_PREFIX = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyChAZIcZj7oqPZscN3_I846NmJHb2nX_f8&cx=004459222364309715284:-umvhhkr0tw&q='
OPTIONAL_PARAMS = '&sort=date'

# Set the route and accepted methods
@mod_parser.route('/<stock_name>', methods=['GET', 'POST'])
def parse(stock_name):
    response_dict = query_by_string(stock_name)
    item_list = response_dict.get('items')
    for item in item_list:
        snippet = item['snippet']
        get_date_from_snippet(snippet)

    return jsonify(items=item_list)


def query_by_string(stock_name):
    query = QUERY_PREFIX + stock_name
    r = requests.get(query)
    response_dict = r.json()

    print 'all response keys: {}'.format(response_dict.keys())
    item_list = response_dict.get('items')
    print 'all item keys: {}'.format(item_list[0].keys())

    return response_dict


def get_date_from_snippet(snippet):

    cyear  = '年'.decode("utf8")
    cdate  = '日'.decode("utf8")
    cmonth = '月'.decode("utf8")
    cdate  = '日'.decode("utf8")

    date = re.search('\d+' + cyear + '\d+'+ cmonth +'\d+' + cdate, snippet, 0)
    if date:
        print date.group()
        return date.group()
    else:
        print snippet
        return snippet
