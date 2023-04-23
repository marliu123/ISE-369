#113434693
#Marcus Liu
import pandas as pd
import geopandas
from matplotlib import pyplot as plt

#Step 1
fl_cd = geopandas.read_file('fl_cong_adopted_2022.zip')
fl_cd.plot()
plt.title('Florida Congressional Districts')
plt.show()


#Step 2
h118 = pd.read_csv('H118.csv', sep=',', header='infer', low_memory=False)
h118 = h118.loc[h118['congress'] == 118]
h118= h118.loc[h118['chamber'] < 'I']
h118FL= h118.loc[h118['state_abbrev'] == "FL"]
nom = h118FL["nominate_dim1"]
#Step 2b
medNomH = h118["nominate_dim1"].median()
print("Step 2b")
print("Median nominate value for House members is:", medNomH)
#Step 2c
medNomHFL = h118FL["nominate_dim1"].median()
print("Step 2c")
print("Median nominate value for House members in Florida is:", medNomHFL)
#Step 2d
print("Step 2d")
print(f"Florida's median member is more conservative with a value of {medNomHFL} because it has a closer value to 1. -1 means more liberal whereas 1 means conservative. This makes Florida more conservative than overall which is {medNomH}.")
#Step 3
print("Step 3")
fl_cd["nominate_dim1"] = nom.array
print(fl_cd) 
#Step 4
print("Step 4")
fl_cd.plot(column='nominate_dim1', cmap="bwr", legend=True, vmin=-1, vmax=1, edgecolor='black',
           legend_kwds={'label': "NOMINATE Ideology Values",'orientation': "horizontal"})
plt.title('Florida Nominate Ideology')
plt.show()