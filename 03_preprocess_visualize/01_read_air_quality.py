import pandas as pd
#df = pandas.read_csv("AirQualityUCI.csv", sep = ";", decimal = ",")
dataFrame = pd.read_csv("../csv_data/AirQualityUCI.csv")
# Resgape the dateFrame index location
df = dataFrame.iloc[:, 0:14]
print ('df/head():', df.head())

df = df[df['Date'].notnull()]
print ('df.isna().sum():', df.isna().sum())

df['DateTime'] = (df.Date) + ' ' + (df.Time)
print ('\ntype(df.DateTime[0]):')
print (type(df.DateTime[0]))

import matplotlib.pyplot as plt


plt.plot(df['T'])
plt.show()
# plt.plot(df['RH'])
# plt.show()
plt.plot(df['C6H6(GT)'])
plt.show()

plt.boxplot(df[['T','C6H6(GT)']].values)
plt.show()