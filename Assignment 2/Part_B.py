import pandas as pd
import geopandas
import matplotlib.pyplot as plt


fl_cd = geopandas.read_file('fl_cong_adopted_2022.zip')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_csv('weball22.txt', sep='|', header=None)
df = df.loc[:, [0, 1, 2, 4, 5, 7, 18, 19]]
df = df.rename(columns = {0:"ID"})
df = df.rename(columns = {1:"Name"})
df = df.rename(columns = {2:"I/C"})
df = df.rename(columns = {4:"Party"})
df = df.rename(columns = {5:"$$"})
df = df.rename(columns = {7:"Disbursement"})
df = df.rename(columns={18: "State"})
df = df.rename(columns={19: "District"})
df = df.loc[df['ID'] < 'I']
df_fl = df.loc[df['State'] == 'FL']
fl_cd = fl_cd.loc[0:7, :]
fl_cd['winner'] = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'D']
fl_cd['diff'] = [3, 2, 2, 2, 3, 1, 3, -1]
dr = fl_cd.plot(column='diff', cmap='bwr', legend=True, vmin=-3, vmax=3)
title = "Margin of Victory Per District"
plt.title(title)
plt.show()
