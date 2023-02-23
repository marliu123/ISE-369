import geopandas
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('/Users/marcusliu/Documents/ISE-369')
ny_cd = geopandas.read_file('ny_cong_adopted_2022.zip')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(ny_cd)
print('Available styles', plt.style.available)
styles = plt.style.available
for s in styles:
    plt.style.use(s)
    ny_cd.plot()
    plt.title(s)
    plt.show()
