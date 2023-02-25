import pandas as pd
import os
os.chdir('/Users/marcusliu/Documents/ISE-369')

def format(x):
    return "${:.2f}M".format(x/1000000)

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

df2 = df
df2 =df2.loc[df2['State'] == 'FL']
df2 = df2.loc[df2['District'] == 1.0]
df2 = df2.sort_values('$$', ascending=False)
print("State: Florida")
print("District: 1.0")
print("8. What individual in your district raised the most amount of money?")
print(df2.iat[0,1], "raised the most money. They raised", format(df2.iat[0,4]))
print("a. Is this individual a Republican or Democrat?")
print("This individual is a", df2.iat[0,3])
print("b. Is this individual an incumbent or challenger?")
print("This individual is a", df2.iat[0,2])

df3 = df2
df3 = df3.sort_values('Disbursement', ascending=False)
df3["Disbursement"] = df3["Disbursement"].apply(format)
print("\n2. Which individual spent the most money? How much money?")
print( df3.iat[0,1], "spent the most money. They spent", df3.iat[0,5])
print("a. Is this individual a Republican or Democrat?")
print("This individual is a", df3.iat[0,3])
print("b. Is this individual an incumbent or challenger?", df3.iat[0,2])

df4 = df2
df4=df4.loc[df4['I/C'] == 'I']
I = df4["$$"].sum()
df5 = df2
df5=df5.loc[df5['I/C'] == 'C']
C = df5["$$"].sum()
print("\nBased on the OpenFEC data, did the incumbent or challenger(s) raise more campaign contributions? How much money?")
if(I > C):
    print("Incumbents raised more campaign contributions. They raised $", I)
else:
    print("Challengers raised more campaign contributions. They raised $", C)

df6 = df2
df6=df6.loc[df6['I/C'] == 'I']
I = df6["Disbursement"].sum()
df7 = df2
df7=df7.loc[df7['I/C'] == 'C']
C = df7["Disbursement"].sum()
print("Based on the OpenFEC data, did the incumbent or challenger(s) spend more campaign contributions? How much money?")
if(I > C):
    print("Incumbents spent more campaign contributions. They spent $", I)
else:
    print("Challengers spent more campaign contributions. They spent $", C)

