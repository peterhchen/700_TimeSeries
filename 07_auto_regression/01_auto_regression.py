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
# Show ACP
split = len(df) - int (0.2* len(df))
train, set = df['T'][0:split], df['T'][split:]
from statsmodels.graphics.tsaplots import plot_acf

import matplotlib.pyplot as plt
plot_acf(train, lags = 100)
plt.show()