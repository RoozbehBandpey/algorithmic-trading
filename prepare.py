import quandl
from pprint import pprint\

# mydata = quandl.get("BITFINEX/ETHUSD")



class loader():
	def __init__(self):
		"""
		Loads data from virenty of sources
		"""

	def get_eth_eur_bitfinex(self):
		"""
		Loads eherium vs euro data from BITFINEX
		"""		
		return quandl.get_table("BITFINEX/ETHUSD")
