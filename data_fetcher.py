#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas numpy requests plotly statsmodels schedule')


# In[3]:


import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


# In[4]:


def fetch_fx_data(pair="EURUSD=X",period="60d",interval="1h"):
    data=yf.download(
        tickers=pair,
        period=period,
        interval=interval,
        auto_adjust=True #adjusts any splits/dividends
        
    )
    data.columns=data.columns.droplevel(1)
    data['Volume']=data['Volume'].replace(0,1)
    if data.empty:
        raise ValueError(f"No data returned for {pair}")
    return data
if __name__=="__main__":
    df=fetch_fx_data()
    print(df.shape)
    print(df.head(5))
    df.to_csv("raw_fx_data")


# In[5]:


da.to_parquet("data_fetcher_op.parquet")


# In[ ]:




