import quandl
from pprint import pprint\

mydata = quandl.get("BITFINEX/ETHUSD")
print(len(mydata))

pprint(mydata)
