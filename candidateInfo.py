import pandas as pd
import os
os.chdir('/Users/marcusliu/Documents/ISE-369')
df = pd.read_csv('weball22.txt', sep='|', header=None)
df=df.loc[:,[0,1,2,4,5,18,23]]
df = df.rename(columns = {0:"ID"})
df = df.rename(columns = {1:"Name"})
df = df.rename(columns = {2:"I/C"})
df = df.rename(columns = {4:"Pty"})
df = df.rename(columns = {5:"$$"})
df = df.rename(columns = {18:"State"})
df = df.rename(columns = {23:"Status"})
df = df.sort_values('$$', ascending=False)

def format(x):
    return "${:.2f}M".format(x/1000000)
df['$$'] = df['$$'].apply(format)
print("Top 25")
print(df.head(25))