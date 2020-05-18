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
# First Naive Method
print ("\ndf['T']:")
print(df['T'])
df['T_t-1'] = df['T'].shift(1)
df_naive = df[['T', 'T_t-1']][1:]
# print ("\ndf[['T', 'T_t-1']]:")
# print(df[['T', 'T_t-1']])
# df[['T', 'T_t-1']]:
#         T  T_t-1
#0     13.6    NaN
#1     13.3   13.6
# print ("\ndf[['T', 'T_t-1']][1:]:")
# print(df[['T', 'T_t-1']][1:])
# df[['T', 'T_t-1']]:
#         T  T_t-1
#1     13.3   13.6
print ("\ndf_naive:")
print(df_naive)
from sklearn import metrics
from math import sqrt
true = df_naive['T']
prediction = df_naive['T_t-1']
error = sqrt (metrics.mean_squared_error (true, prediction))
print ('RMSE for Naive Method 1:', error)
# Second naive Method
df['T_rm'] = df['T'].rolling(3).mean().shift(1)
df_naive = df[['T', 'T_rm']].dropna()       # drop out not a number
true = df_naive ['T']
prediction = df_naive ['T_rm']
print ("\ndf_naive['T_rm']:")
print(df_naive['T_rm'])
error = sqrt(metrics.mean_squared_error (true, prediction))
print ('RMSE for Naive Method 2:', error)
