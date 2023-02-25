import geopandas
import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('/Users/marcusliu/Documents/ISE-369')
fl_cd = geopandas.read_file('fl_cong_adopted_2022.zip')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
geom_cd1 = fl_cd.at[0, 'geometry']
print("type of geom_cd1 is", geom_cd1.geom_type)
print("Area of CD! is ", geom_cd1.area)
print("Length of CD! is ", geom_cd1.length)
print('Available styles', plt.style.available)
print(geom_cd1)
styles = plt.style.available
for s in styles:
    plt.style.use(s)
    fl_cd.plot()
    plt.title('FL Congressional Districts')
    plt.title(s)
    plt.show()
