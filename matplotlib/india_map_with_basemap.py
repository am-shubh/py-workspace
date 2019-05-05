import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fontDict = {
	'family': 'serif',
	'color': 'cyan',
	'size': 10
}

_map = Basemap(projection='mill',
	llcrnrlat = 7.028213,
	llcrnrlon = 67.608505,
	urcrnrlat = 37.112376,
	urcrnrlon = 99.583285)

# 7.028213, 67.608505   7.263440, 68.543554

_map.drawcoastlines()
_map.drawcountries(linewidth=2)
# _map.drawmapboundary(fill_color='aqua')
# _map.fillcontinents()

_map.bluemarble()

newDelhi_lat, newDelhi_lon = 28.6139, 77.2090
xpt, ypt = _map(newDelhi_lon, newDelhi_lat)

india_lat, india_lon = 20.5937, 78.9629
xpt1, ypt1 = _map(india_lon, india_lat)

_map.plot(xpt, ypt, 'r*', markersize=10)

plt.text(xpt, ypt,'New Delhi', fontdict = fontDict)
plt.text(xpt1, ypt1,'INDIA', fontdict = fontDict)

plt.title('India Map')
plt.show()
