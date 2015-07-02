In [1]: import pandas as pd

In [2]: import numpy as np

In [3]: import statsmodels.api as sm

In [4]: loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


In [5]: 

In [5]: x = loansData['Interest.Rate'][0:5].values[1]

In [6]: x = x.rstrip('%')

In [7]: x = float(x)

In [8]: x = x / 100

In [9]: x = round(x, 4)

In [10]: y = lambda x: round(float(x.rstrip('%')) / 100, 4)

In [11]: cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))

In [12]: loansData['Interest.Rate'] = cleanInterestRate

In [13]: cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))

In [14]: loansData['Loan.Length'] = cleanLoanLength

In [15]: loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

In [16]: import matplotlib.pyplot as plt

In [17]: intrate = loansData['Interest.Rate']

In [18]: loanamt = loansData['Amount.Requested']

In [19]: fico = loansData['FICO.Score']

In [20]: y = np.matrix(intrate).transpose()

In [21]: x1 = np.matrix(fico).transpose()

In [22]: x = np.column_stack([x1,x2])
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-22-e3f7393d11d6> in <module>()
----> 1 x = np.column_stack([x1,x2])

NameError: name 'x2' is not defined

In [23]: x2 = np.matrix(loanamt).transpose()

In [24]: x = np.column_stack([x1,x2])

In [25]: X = sm.add_constant(x)

In [26]: model = sm.OLS(y,X)

In [27]: f = model.fit()

In [28]: f.summary)_
  File "<ipython-input-28-455775380034>", line 1
    f.summary)_
             ^
SyntaxError: invalid syntax


In [29]: f.summary()
Out[29]: 
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.657
Model:                            OLS   Adj. R-squared:                  0.656
Method:                 Least Squares   F-statistic:                     2388.
Date:                Wed, 01 Jul 2015   Prob (F-statistic):               0.00
Time:                        20:37:10   Log-Likelihood:                 5727.6
No. Observations:                2500   AIC:                        -1.145e+04
Df Residuals:                    2497   BIC:                        -1.143e+04
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          0.7288      0.010     73.734      0.000         0.709     0.748
x1            -0.0009    1.4e-05    -63.022      0.000        -0.001    -0.001
x2          2.107e-06    6.3e-08     33.443      0.000      1.98e-06  2.23e-06
==============================================================================
Omnibus:                       69.496   Durbin-Watson:                   1.979
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               77.811
Skew:                           0.379   Prob(JB):                     1.27e-17
Kurtosis:                       3.414   Cond. No.                     2.96e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.96e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
