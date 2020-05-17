import pandas as pd
#df = pandas.read_csv("AirQualityUCI.csv", sep = ";", decimal = ",")
dataFrame = pd.read_csv("../csv_data/GOOG.csv")
# Resgape the dateFrame index location
df = dataFrame.iloc[:, 0:14]
print ('df/head():', df.head())

df = df[df['Date'].notnull()]
print ('df.isna().sum():', df.isna().sum())

import matplotlib.pyplot as plt


plt.plot(df['Adj Close'])
plt.xlabel('Time') 
plt.ylabel('Price')
plt.title('Google')
plt.show()

df['Volume'] = df['Volume']/1000
plt.plot(df['Volume'])
plt.xlabel('Time') 
plt.ylabel('Volumn x 1000')
plt.title('Google')
plt.show()

plt.boxplot(df[['Adj Close','Volume']].values)
plt.xlabel('Time') 
plt.ylabel('Price, Volumn x 1000')
plt.title('Google')
plt.show()