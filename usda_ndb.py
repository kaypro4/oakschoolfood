# USDA National Nutrient Database Integration
from __future__ import absolute_import, division, print_function
import requests

USDA_NDB_API_PATH = 'http://api.nal.usda.gov/ndb/'


def search(api_key, search_term):
    """ http://ndb.nal.usda.gov/ndb/doc/apilist/API-SEARCH.md

    Internal params of interest
    Sort the results by food name (n) or by search relevance (r)"""

    url_path = USDA_NDB_API_PATH + 'search/'
    payload = {'api_key': api_key, 'format' : 'json', 'q' : search_term, 'sort' : 'r', 'max' : '25','offset' : '0'}
    response = requests.get(url_path, params=payload)
    return response.json()


def food_report(api_key, ndbno):
    """ http://ndb.nal.usda.gov/ndb/doc/apilist/API-FOOD-REPORT.md

    Internal params of interest
    type    n   b (basic)   Report type: [b]asic or [f]ull or [s]tats"""

    url_path = USDA_NDB_API_PATH + 'reports/'
    payload = {'api_key': api_key, 'format' : 'json', 'ndbno' : ndbno, 'type' : 'b'}
    response = requests.get(url_path, params=payload)

    return response.json()


def kcal_for_ndbno(api_key, ndbno):
    """convenience function to get kcals for a food item"""

    NUTRIENT_ID_ENERGY = "208"
    report = food_report(api_key, ndbno)

    # error handling is for losers
    nutrients = report["report"]["food"]["nutrients"]
    for nutrient in nutrients:
        id = nutrient["nutrient_id"]
        if id == NUTRIENT_ID_ENERGY:
            return nutrient["value"]
