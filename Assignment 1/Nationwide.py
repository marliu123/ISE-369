import pandas as pd
import os
os.chdir('/Users/marcusliu/Documents/ISE-369')
df = pd.read_csv('weball22.txt', sep='|', header=None)

df=df.loc[df[0] < 'I']
df2 =df.loc[:,[0, 1, 2, 4,17]]
df2 = df2.sort_values(17, ascending=False)
def format(x):
    return "${:.2f}M".format(x/1000000)
df2[17] = df2[17].apply(format)
print("1. Which individual raised the most campaign money? How much money?")
print( df2.iat[0,1], "raised the most campaign money. They raised", df2.iat[0,4])
print("a. Is this individual a Republican or Democrat?")
print("This individual is a", df2.iat[0,3])
print("b. Is this individual an incumbent or challenger?")
print("This individual is a", df2.iat[0,2])

df3 = df.loc[:,[0, 1, 2, 4, 7 ]]
df3[7] = df3[7].apply(format)
df3 = df3.sort_values(7, ascending=False)
print("\n2. Which individual spent the most campaign money? How much money?")
print( df3.iat[0,1], "spent the most campaign money. They spent", df3.iat[0,4])
print("a. Is this individual a Republican or Democrat?")
print("This individual is a", df3.iat[0,3])
print("b. Is this individual an incumbent or challenger?", df3.iat[0,2])

