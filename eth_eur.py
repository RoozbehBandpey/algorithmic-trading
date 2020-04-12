import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import matplotlib.dates as dates
import numpy as np
from prepare import Loader


def graph_raw_fx():
	loader = Loader()
	data = loader.get_eth_eur_bitfinex()

	print(data)

graph_raw_fx()
