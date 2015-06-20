corsi = [55, 54, 53, 53, 52, 52, 52, 51, 44, 46, 44]

import collections

c = collections.Counter(corsi)

print c

corsi_sum = sum(c.values())

for k,v in c.iteritems():
	print "The frequency of possession " + str(k) + "is" + str(float(v) / corsi_sum)

import matplotlib.pyplot as plt

plt.boxplot(corsi)
plt.show()
plt.savefig(“corsi_boxplot.png”)

plt.hist(corsi, histtype='bar’)
plt.show()
plt.savefig(“corst_hist.png”)

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

corsi = np.random.normal(size=100)
graph1 = stats.probplot(corsi, dist="norm", plot=plt)
plt.show()
plt.savefig(“qq1.png”)

corsi2 = np.random.uniform(size=100)
qq2 = stats.probplot(qq2, dist=“norm”, plot=plt)
plt.show()
plt.savefig(“qq2.png”)
