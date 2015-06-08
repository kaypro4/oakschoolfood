# oakschoolfood
Hacking the Oakland school lunch program

Some resources developed during the National Day of Civic Hacking.

# Menu Processor
process\_menu.py is a first cut at code to parse an OUSD (Oakland Unified
School District) menu and look up calorie counts for each item.

It can be run with the command

python process\_menu.py

and has been tested only with Python 3.4.

To run it, you will need to get an API key from api.data.gov and add it to
a local config file named config.py. The line in that file should look like:

API\_DATA\_GOV\_KEY = 'YOURAPIKEY'

The current code reads in raw menu text from sample\_menu.txt. The text is
parsed into separate menu items and the nutritional content for each menu item
is looked up using the USDA National Nutrient database. Specifically, a
"best match" search is done and the top pick is used. Then, the calorie content
is retrieved for that match. The best match is often not a particularly
good match.

## TODOs
Maybe turn these into GitHub issues.

* Split items with connectors (e.g., hamburger w fries) into separate items
so they can be looked up separately on the USDA site
* Fight with OAUTH and the Python wrapper for Fat Secret, maybe converting
it to Python 3, to bend it to my will (though at the same time fearing
it doesn't add any value on top of the USDA site for our purposes)
* Abstract out the menu parser so parsers can be written for other sources
* Automate extraction of menu text from OUSD PDFs on the website
* Try to get OUSD to share the source text going into Nutrikids to create
the menus
* Write a better matcher than the USDA one
* Clean up the skanky code that comes with hack day projects
