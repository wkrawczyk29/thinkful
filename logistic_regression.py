# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import math
import scipy.stats as stats
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
ld = loansData
ld['Interest.Rate'] = ld['Interest.Rate'].map(lamda x: str(x)[:-1]).astype(float)
x = loansData['Interest.Rate'][0:5].values[1]
x = r.strip('%')
x = x.rstrip('%')
x = float(x)
x = x / 100
x = round(x, 4)
y = lambda x: round(float(x.rstrip('%')) / 100, 4)
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months'))
)
loansData['Loan.Length'] = cleanLoanLength
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
loansData['Low.Interest.Rate'] = loansData['Interest.Rate'] < .12
loansData['Constant_Intercept'] = 1
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Funded.By.Investors']
fico = loansData['FICO.Score']
intercept = loansData['Constant_Intercept']
ind_var = ['Constant_Intercept', 'Amount.Funded.By.Investors', 'FICO.Score']
logit = sm.Logit(loansData['Low.Interest.Rate'], loansData[ind_var])
result = logit.fit()
coeff = result.params
print result.summary()
print coeff
print coeff[1]
print coeff[2]
print coeff[0]
def logistic_function(ficoScore, loanAmt)
def logistic_function(ficoScore, loanAmt):
    logit = sm.Logit(ld['Low.Interest.Rate'], ld[ind_var])
    result = logit.fit()
    coeff = result.params
    p = 1/(1 + math.e^(coeff[0] + coeff[2] * ficoScore + coeff[1] * loanAmt))
    return p
print logistic_function(720, 10000)
def logistic_function(ficoScore, loanAmt):
    logit = sm.Logit(ld['Low.Interest.Rate'], ld[ind_var])
    result = logit.fit()
    coeff = result.params
    p = 1/(1 + math.e**(coeff[0] + coeff[2] * ficoScore + coeff[1] * loanAmt))
    return p
print logistic_function(720, 10000)
#probabily is .27 % chance of acceptance
#probability is 27% chance of acceptance which seems low
