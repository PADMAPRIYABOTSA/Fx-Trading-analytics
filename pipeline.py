#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from datetime import datetime
from dashboard import create_dashboard


# In[19]:


def run_pipeline(pairs=["EURUSD=X","GBPUSD=X","USDJPY=X"]):
    timestamp=datetime.now().strftime("%Y%m%d_%H%M")
    all_results={}
    for pair in pairs:
        try:
            analytics_df=pd.read_parquet("analytic_output.parquet")
            if pair=="EURUSD=X":
                create_dashboard(analytics_df)
            all_results[pair]={
                "rows" : len(analytics_df),
                "latest_close": round(analytics_df['Close'].iloc[-1],5),
                "avg_vol": round(analytics_df['realized_volatility'].mean(),4),
                "current_signal": int(analytics_df['momentum_signal'].iloc[-1])
            }
        except Exception as e:
            print(f" ERROR processing {pair}:{e}")
            all_results[pair]={"error":str(e)}
    summary_df=pd.DataFrame(all_results).T
    return summary_df
run_pipeline()


# In[ ]:




