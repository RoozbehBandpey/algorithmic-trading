import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import matplotlib.dates as dates
import numpy as np
from prepare import Loader


def graph_raw_fx():
	loader = Loader()
	data = loader.get_eth_eur_bitfinex()
	high, low, mid, last, bid, ask, volume = np.load(data)
	# high = np.load(data)

	print(high)

graph_raw_fx()
