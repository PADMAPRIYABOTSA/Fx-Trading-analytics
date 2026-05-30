#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np
df=read_parquet("data_fetcher_op.parquet")


# In[ ]:


df.columns
df.shape
df.head(10)


# In[ ]:





# In[ ]:


def calculate_realized_volatility(data,window=24):
    log_returns=np.log(data['Close']/data['Close'].shift(1))
    realized_vol=log_returns.rolling(window=window).std()*np.sqrt(24*252)
    return realized_vol
def calculate_vwap(data,window=24):
    typical_price=(df['High']+df['Low']+df['Close'])/3
    price_volume=typical_price*df['Volume']
    vwap=(
        price_volume.rolling(window=window).sum()/df['Volume'].rolling(window=window).sum()
    )
    return vwap
def calculate_momentum(data,short=4,long=24):
    short_ma=df['Close'].rolling(window=short).mean()
    long_ma=df['Close'].rolling(window=long).mean()
    momentum_signal=np.sign(short_ma-long_ma)
    return momentum_signal
def calculate_spread_proxy(data,window=24):
    spread_proxy=(df['High']-df['Low'])/df['Close']
    rolling_spread=spread_proxy.rolling(window=window).mean()
    return rolling_spread
def run_all_analytics(df):
    results=df.copy()
    results['realized_volatility']=calculate_realized_volatility(df)
    results['vwap']=calculate_vwap(df)
    results['momentum_signal']=calculate_momentum(df)
    results['rolling_spread']=calculate_spread_proxy(df)
    results['price_vs_vwap']=((results['Close']-results['vwap'])/results['vwap'])*100
    results=results.dropna(subset=['realized_volatility','vwap'])
    return results


# In[ ]:


analytics=run_all_analytics(df)
analytics.head(10)


# In[ ]:


analytics.to_parquet("analytic_output.parquet")


# In[ ]:




