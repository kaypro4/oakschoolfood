
from fatsecret import * 
from config import * 
from datetime import *
from pandas import *

#-----------------------------------
#To get this working you'll need to add a config.py file with these two lines:
#consumer_key='YOURKEYHERE'
#consumer_secret='YOURKEYHERE'
#get your keys here: http://platform.fatsecret.com/api/ 

fs=Fatsecret(consumer_key,consumer_secret)

#for now, search expressions cannot contain spaces
result=fs.foods_search("Chinese Chicken Salad")
print result

