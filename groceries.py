#!/usr/bin/env python2
import os
from urllib import urlencode
from urllib2 import urlopen

from lxml.etree import fromstring

APIKEY = os.environ['SUPERMARKETAPI_APIKEY']

def get_xml(url):
    'Download a url and parse it to an XML tree.'
    handle = urlopen(url)

    # Remove the schema
    text = handle.readline()
    text += handle.readline().split(' ')[0] + '>\r\n'
    text += handle.read()

    return fromstring(text)

def stores(state, city):
    'Get an array of stores for a given city.'
    params = urlencode({
        'APIKEY': APIKEY,
        'SelectedState': state,
        'SelectedCity': city,
    })
    url = 'http://www.SupermarketAPI.com/api.asmx/StoresByCityState?' + params
    return get_xml(url)

def store_ids(state, city):
    'Get a list of storeIds for a given city.'
    return map(unicode, stores(state, city).xpath('//StoreId/text()'))

def search_for_item(store_id, item_name):
    url = 'http://www.SupermarketAPI.com/api.asmx/SearchForItem?APIKEY=%s&StoreId=%s&ItemName=%s' % (APIKEY, store_id, item_name)
    return get_xml(url)
