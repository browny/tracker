# -*- coding: utf-8 -*-

from flask import current_app
import requests
import re


def query_by_string(stock_name):
    api_key = current_app.config['GOOGLE_API_KEY']
    search_engine_id = current_app.config['GOOGLE_SEARCH_ENGINE_ID']

    QUERY = 'https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q='
    FORMAT_QUERY = QUERY % (api_key, search_engine_id)
    OPTIONAL_PARAMS = '&sort=date'

    query = FORMAT_QUERY + stock_name + OPTIONAL_PARAMS

    print 'query: {}'.format(query.encode('utf-8').strip())

    r = requests.get(query.encode('utf-8').strip())
    response_dict = r.json()

    item_list = response_dict.get('items')
    print 'all response keys: {}'.format(response_dict.keys())
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

