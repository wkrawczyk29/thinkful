import matplotlib.pyplot as plt

import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested')
plt.savefig(“Amount_Request_Hist.png”)
plt.show()

loansData.hist(column=‘Amount.Requested’)
plt.savefig(“Amount_Request_box.png”)
plt.show()

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig(“Amount_Requested_QQ.png”)
plt.show()
