import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

os.chdir('/Users/marcusliu/Documents/ISE-369')
#with open('anes_timeseries_2020.csv') as f:
#   contents = f.read()


#Q1
print("Question 1:")
anes = pd.read_csv('anes_timeseries_2020.csv', sep=',', header='infer', low_memory=False)
anes = anes[['V201033', 'V201156', 'V201157', 'V201200']].copy()
print(anes)

#Q2
print("Question 2:")
anes['PresidentVote'] = anes['V201033'].replace([11,12,-1,-8,-9], np.nan)
print(anes)

#Q3
print("Question 3:")
DemNum = anes['PresidentVote'].value_counts()[1]
RepNum = anes['PresidentVote'].value_counts()[2]
vote_share = DemNum / (DemNum + RepNum)
print(vote_share)

#Q4
biden = 81268924
trump = 74216154
both = biden + trump
percent = biden / both
difference = vote_share - percent
print("Question 4a:")
print(f"Biden’s share of the two-party vote according to the FEC report was :", percent)
print("Question 4b:")
print(f"The survey results were {difference} percent (55.5 percent) from the actual 2020 election results.")

#Q5
print("Question 5:")
anes["DemFeel"]=anes['V201156'].replace([-9,998,999], np.nan)
anes["RepFeel"]=anes['V201157'].replace([-9,998,999], np.nan)
anes["Ideology"]=anes['V201200'].replace([-9,-8,99], np.nan)
print(anes)

#Q6
sns.scatterplot(x="DemFeel",y="RepFeel",
                data=anes,
                hue='Ideology',
                palette=['darkblue','blue','dodgerblue','gray','lightcoral','red','darkred'],
                alpha=0.5).set(title="Feelings from Democratic and Republican Parties")
plt.show()