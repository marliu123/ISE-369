import geopandas
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('/Users/marcusliu/Documents/ISE-369')
ny_cd = geopandas.read_file('ny_cong_adopted_2022')
for i in range(len(ny_cd)) :
    print(i, 'Congressional District ', ny_cd.loc[i, "DISTRICT"])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
geom_cd1 = ny_cd.at[0, 'geometry']
ny_cd_4326 = ny_cd.to_crs("EPSG:4326")
ny_cd_4326.plot()
plt.title('NY Congressional Districts-4326')
plt.show()

import contextily as cx
li_cd = ny_cd.loc[0:0,:]
print('LI coordinate system is ', li_cd.crs)
li_cd_wm = li_cd.to_crs(epsg=3857)
print('New LI cordinate system is ', li_cd_wm.crs)
lx = li_cd_wm.plot(figsize=(15, 10), alpha=0.5, edgecolor='k')
cx.add_basemap(lx, crs=li_cd_wm.crs)
plt.show()