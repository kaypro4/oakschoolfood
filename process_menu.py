from __future__ import absolute_import, division, print_function
import config
import fatsecret
import menu_cleaner
import usda_ndb


def usda_menu_item_lookup(menu_item):
    search_response = usda_ndb.search(config.API_DATA_GOV_KEY, menu_item)
    # print(search_response)
    if 'list' in search_response:
        # success
        result_count = int(search_response["list"]["total"])
        # print("Results found: {0}".format(result_count))
        if result_count > 0:
            first_item = search_response["list"]["item"][0]
            name = first_item["name"]
            ndbno = first_item["ndbno"]
            kcal = usda_ndb.kcal_for_ndbno(config.API_DATA_GOV_KEY, ndbno)
            print("Best match: {0}".format(name))
            print("Calories: {0}".format(kcal))
    else:
        # No match found or something bad happened
        print("No match for {0}".format(menu_item))

        # If menu_item is 2+ words, remove first and try again
        # Some of the descriptions have adjectives that confuse the matcher
        word, space, rest = menu_item.partition(' ')
        usda_menu_item_lookup(rest)


def fatsecret_menu_item_lookup(menu_item):
    fs = fatsecret.Fatsecret(config.consumer_key, config.consumer_secret)
    # for now, search expressions cannot contain spaces
    result = fs.foods_search(menu_item)
    print(result)

if __name__ == '__main__':
    # Get a list of food items from raw menu text
    cleaned = menu_cleaner.clean_menu('sample_menu.txt')
    # print(cleaned)

    for menu_item in cleaned:
        print("Menu item: {0}".format(menu_item))

        usda_menu_item_lookup(menu_item)

        # no workie due to OAUTH woes
        #fatsecret_menu_item_lookup(menu_item)
