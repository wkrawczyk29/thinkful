import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
   ...:    ...: North, 6.47, 4.03
   ...:    ...: Yorkshire, 6.13, 3.76
   ...:    ...: Northeast, 6.19, 3.77
   ...:    ...: East Midlands, 4.89, 3.34
   ...:    ...: West Midlands, 5.63, 3.47
   ...:    ...: East Anglia, 4.52, 2.92
   ...:    ...: Southeast, 5.89, 3.20
   ...:    ...: Southwest, 4.79, 2.71
   ...:    ...: Wales, 5.27, 3.53
   ...:    ...: Scotland, 6.08, 4.51
   ...:    ...: Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0]

data_rows = data[1::]

df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

df.describe()

for i in df:
    x = df['Alcohol'].mean()
    y = df['Tobacco'].mean()
print “The The mean of Alcohol and Tobacco are {}, {}".format(x, y)

for i in df:
    x = df['Alcohol'].median()
    y = df['Tobacco'].median()
print “ The median is {}, {}".format(x, y)

for i in df:
    x = stats.mode(df['Alcohol'])
    y = stats.mode(df['Tobacco'])
print “The mode of Alcohol & Tobacco are {}, {}".format(x, y)

for i in df:
    x = max(df['Alcohol']) - min(df['Alcohol'])
    y = max(df['Tobacco']) - min(df['Tobacco'])
print "The range of Alchy and Tobaccy is {}, {}".format(x, y)

for i in df:
    x = df['Alcohol'].std()
    y = df['Tobacco'].std()
print "The deviation of Alchy and Tobaccy is {}, {}".format(x, y)

for i in df:
    x = df['Alcohol'].var()
    y = df['Tobacco'].var()
print "The variance for Alchy and Tobaccy is {}, {}".format(x, y)
