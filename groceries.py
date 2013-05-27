#!/usr/bin/env python2
import os

from lxml.etree import parse, XMLParser

APIKEY = os.environ['SUPERMARKETAPI_APIKEY']

def stores(state, city):
    params = (APIKEY, state, city)
    url = 'http://www.SupermarketAPI.com/api.asmx/StoresByCityState?APIKEY=%s&SelectedState=%s&SelectedCity=%s' % params
    array_of_store = parse(url, XMLParser(dtd_validation=True))
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
