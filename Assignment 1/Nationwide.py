import pandas as pd
import os
os.chdir('/Users/marcusliu/Documents/ISE-369')
df = pd.read_csv('weball22.txt', sep='|', header=None)
df =df.loc[:,[0,1,2,4,5,7,17,18,19,23]]
df = df.rename(columns = {0:"ID"})
df = df.rename(columns = {1:"Name"})
df = df.rename(columns = {2:"I/C"})
df = df.rename(columns = {4:"Party"})
df = df.rename(columns = {5:"$$"})
df = df.rename(columns = {7:"Disbursement"})
df = df.rename(columns = {17:"Ind_Contr"})
df = df.rename(columns = {18:"State"})
df = df.rename(columns = {19:"District"})
df = df.rename(columns = {23:"Status"})
df =df.loc[df['ID'] < 'I']

def format(x):
    return "${:.2f}M".format(x/1000000)





df2 = df
df2 = df2.sort_values('$$', ascending=False)
df2["$$"] = df2["$$"].apply(format)
print("1. Which individual raised the most campaign money? How much money?")
print( df2.iat[0,1], "raised the most campaign money. They raised", df2.iat[0,4])
print("a. Is this individual a Republican or Democrat?")
print("This individual is a", df2.iat[0,3])
print("b. Is this individual an incumbent or challenger?")
print("This individual is a", df2.iat[0,2])

df3 = df
df3 = df3.sort_values('Disbursement', ascending=False)
df3["Disbursement"] = df3["Disbursement"].apply(format)
print("\n2. Which individual spent the most campaign money? How much money?")
print( df3.iat[0,1], "spent the most campaign money. They spent", df3.iat[0,5])
print("a. Is this individual a Republican or Democrat?")
print("This individual is a", df3.iat[0,3])
print("b. Is this individual an incumbent or challenger?", df3.iat[0,2])

df4 = df 
df4 = df4.loc[df4['Party'] == 'DEM']
print("\n3. What is the mean (or average) amount of campaign expenditures for Democrats?")
print("The average amount of campaign expenditures for Democrats were", format(df4["Disbursement"].mean()))

df5 = df
df5 = df5.loc[df5['Party'] == 'REP']
print("\n4. What is the mean (or average) amount of campaign expenditures for Republicans?")
print("The average amount of campaign expenditures for Republicans were", format(df5["Disbursement"].mean()))

df6 = df
df6 = df6.loc[df6['I/C'] == 'I']
print("\n5. What is the mean (or average) amount of campaign expenditures for Incumbents?")
print("The average amount of campaign expenditures for Incumbents were", format(df6["Disbursement"].mean()))


df7 = df
df7 = df7.loc[df7['I/C'] == 'C']
print("\n6. What is the mean (or average) amount of campaign expenditures for Challengers?")
print("The average amount of campaign expenditures for Challengers were", format(df7["Disbursement"].mean()))

