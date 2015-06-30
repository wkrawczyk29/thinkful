import pandas as pd

import matplotlib.pyplot as plt

from scipy import stats

import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

OpenLines = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

stats.chisquare(OpenLines.values())
