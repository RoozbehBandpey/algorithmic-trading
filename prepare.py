import quandl as q


class Loader():
	QUERY = "BITFINEX/ETHUSD"
	def __init__(self):
		"""
		Loads data from variety of sources
		"""
		self.QUERY = "BITFINEX/ETHUSD"

	def get_eth_eur_bitfinex(self):
		"""
		Loads Etherium vs euro data from BITFINEX
		"""		
		return q.get(self.QUERY, returns='numpy')




if __name__ == "__main__":
	l = loader()
	data = l.get_eth_eur_bitfinex()
	print(data)
