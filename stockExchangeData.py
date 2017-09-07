# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:34:59 2017

@author: Susant Achary
"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pylab import rcParams

stock_data = pd.read_csv("D:\\DataAnalytics\\Datasets\\TCS@NSE.csv")

stock_data.columns
stock_data["Open Price"].hist(bins=50)

stock_data.isnull()

stock_data.boxplot(column="Open Price" , by="Date")

stock_data.dtypes

dateparse = lambda dates:pd.datetime.strptime(dates, '%d-%b-%Y')

stockExchange = pd.read_csv('D:\\DataAnalytics\\Datasets\\TCS@NSE.csv',parse_dates=['Date'],index_col='Date',date_parser=dateparse)

from datetime import datetime
ts = stockExchange["Open Price"]
plt.plot(ts)
plt.xlabel("Date Range")
plt.ylabel("TCS StockPrice")
plt.subtitle("TCS Stock Value over Time Range")

from statsmodels.tsa.stattools import adfuller
def test_stationary(timeseries):
    
    #Determining rolling statistics
    rollingMean = pd.rolling_mean(timeseries,window=12)
    rollingStandardDeviation = pd.rolling_std(timeseries,window = 12)
    
    #plotting rolling statistics:
    original = plt.plot(timeseries,color='blue',label='Original')
    mean = plt.plot(rollingMean,color='red',label='Rolling Mean')
    std = plt.plot(rollingStandardDeviation,color='black',label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block = False)
    
    #perform Dickey-Fuller test:
    print ('Result of Dickey-Fuller Test:')
    dftest = adfuller(timeseries,autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#lags Used','Number of Observations Used'])
    
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)' %key] = value
    print (dfoutput)
    
test_stationary(ts)