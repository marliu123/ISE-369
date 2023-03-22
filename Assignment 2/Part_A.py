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
raised = {}
for i in range(0, 10):
    df_fld = df_fl.loc[df['District'] == i]
    raised[i] = df_fld['$$'].sum()
print(raised)

fl_cd['Contrib'] = raised
fl_cd = fl_cd.to_crs(fl_cd.crs)
fl_cd.plot(column='Contrib', legend=True, figsize=(15, 10), alpha=.85, edgecolor='k')
title = "Florida Congressional Districts Contributions"
plt.title(title)
plt.show()

