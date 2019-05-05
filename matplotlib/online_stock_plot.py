import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

# converting dates into format to display on plot
def bytespdate2num(fmt, encoding='utf-8'):
	strConverter = mdates.strpdate2num(fmt)
	def bytesConverter(b):
		s = b.decode(encoding)
		return strConverter(s)
	return bytesConverter

# fetching data from url
stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source =urllib.request.urlopen(stock_price_url).read().decode()

stock_data = []
split_source = source.split('\n')

# extracting data
for line in split_source:
	split_line = line.split(',')
	if len(split_line) == 7:
		if 'Date' not in line:
			stock_data.append(line)

date, openPrice, highPrice, lowPrice, closePrice, adjustedClosePrice, volume = np.loadtxt(stock_data, delimiter=',', unpack=True, converters={0:bytespdate2num('%Y-%m-%d')})

# function to plot sub graphs
def plot_sub_graph(index:int, yPlotValue, labelValue: str):
	plt.subplot(2, 2, index)
	plt.plot([], [], label='loss', color='r')
	plt.plot([], [], label='gain', color='g')
	plt.plot_date(date, yPlotValue, '-', label = labelValue)

	# coloring loss and gain data
	plt.fill_between(date, yPlotValue, yPlotValue[0], where=(yPlotValue > yPlotValue[0]), facecolor = 'g', alpha=0.5)
	plt.fill_between(date, yPlotValue, yPlotValue[0], where=(yPlotValue < yPlotValue[0]), facecolor = 'r', alpha=0.5)
	
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.xticks(rotation=45,)
	plt.legend()


# generating values to pass in "plot_sub_graph" method for 4 type of data
yPlotValue = [openPrice, highPrice, lowPrice, closePrice]
labelValue = ['Open Prices', 'High Prices', 'Low Prices', 'Close Prices']

for index, (yPlot, label) in enumerate(zip(yPlotValue, labelValue)):
	plot_sub_graph(index+1, yPlot, label)

# give horizontal and vertical space between sub plots
plt.subplots_adjust(wspace=0.40, hspace=0.45)
plt.show()