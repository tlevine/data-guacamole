#!/usr/bin/env python2
import os
from urllib import urlencode
from urllib2 import urlopen

from lxml.etree import fromstring

APIKEY = os.environ['SUPERMARKETAPI_APIKEY']

def stores(state, city):
    'Get an array of stores for a given city.'
    params = urlencode({
        'APIKEY': APIKEY,
        'SelectedState': state,
        'SelectedCity': city,
    })
    url = 'http://www.SupermarketAPI.com/api.asmx/StoresByCityState?' + params
    handle = urlopen(url)

    # Remove the schema
    text = handle.readline()
    text += '<ArrayOfStore>\r\n'
    handle.readline()
    text += handle.read()

    array_of_store = fromstring(text)
    return array_of_store

'''
  <Store>
    <Storename>Gristedes  </Storename>
    <Address>251 W 86th St &amp; Broadway</Address>
    <City>New York</City>
    <State>NY</State>
    <Zip>10024</Zip>
    <Phone> </Phone>
    <StoreId>fdbfe67a44</StoreId>
  </Store>
'''
