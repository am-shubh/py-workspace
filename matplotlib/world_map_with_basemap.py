import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

_map = Basemap(projection='mill')

_map.drawcoastlines()
_map.drawcountries()
_map.drawmapboundary(fill_color='aqua')
_map.fillcontinents(color='coral',lake_color='aqua')

plt.title('World Map')
plt.show()
