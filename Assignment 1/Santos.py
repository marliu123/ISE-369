import pandas as pd
import os

    
os.chdir('/Users/marcusliu/Documents/ISE-369')
df = pd.read_csv('santosfile.csv', sep=',', header=None)
df =df.loc[:,[13, 22]]
df2 = df
df2 = df2.loc[df2[13] == 'NY']
df2[22] = pd.to_numeric(df2[22])


print("7. Locate the “recipient_state” column name.")
print("a. How much did George Santos’s campaign report spending in NY state?")
print("George Santos’s campaign reported spending $",df2[22].sum(), "in NY state")

df3 = df
df3 = df3.drop(0)

print(sum(df3[22]))
print("b. How much did his campaign report spending outside of NY?")
print("George Santo's campaign reported spending $", df3[22].sum(), "outside of NY")



