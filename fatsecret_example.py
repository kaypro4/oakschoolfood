
from fatsecret import * 
from datetime import *
from pandas import *
#-----------------------------------
#get your consumer key and secret after registering 
#as a developer here: http://platform.fatsecret.com/api/ 
consumer_key='10ec942b913647f88743f6451c088b2b'
consumer_secret='eb5d8bb2062a4d7eb3c78d40d9b8968e'

fs=Fatsecret(consumer_key,consumer_secret)

#for now, search expressions cannot contain spaces
result=fs.foods_search("Chinese Chicken Salad")
print result

