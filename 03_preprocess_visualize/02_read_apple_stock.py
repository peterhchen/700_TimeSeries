import pandas as pd
#df = pandas.read_csv("AirQualityUCI.csv", sep = ";", decimal = ",")
dataFrame = pd.read_csv("../csv_data/AAPL.csv")
# Resgape the dateFrame index location
df = dataFrame.iloc[:, 0:14]
print ('df/head():', df.head())

df = df[df['Date'].notnull()]
print ('df.isna().sum():', df.isna().sum())

import matplotlib.pyplot as plt


plt.plot(df['Adj Close'])
plt.show()

plt.plot(df['Volume'])
plt.show()

plt.boxplot(df[['Adj Close','Volume']].values)
plt.show()