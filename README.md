
## Fx-Trading-analytics
Automated FX trading analytics pipeline computing realized volatility, VWAP, momentum signals and spread proxy on EUR/USD, GBP/USD and USD/JPY data.
##Overview
This project builds an automated Python pipeline that fetches hourly FX data 
for three major currency pairs, computes four key microstructure metrics, and 
delivers an interactive multi-panel dashboard. The pipeline is structured in 
modular layers — ingestion, transformation, analytics, visualisation.

## Currency Pairs Covered

| Pair | Description | Why It Matters |
|------|-------------|----------------|
| EUR/USD | Euro / US Dollar | World's most traded pair, ~23% of daily FX volume |
| GBP/USD | British Pound / US Dollar | Highly sensitive to UK macro and rate decisions |
| USD/JPY | US Dollar / Japanese Yen | Key risk sentiment indicator, carry trade benchmark |

## Realized Volatility
Volatility measures how much a price moves over time. Realized volatility is 
calculated from actual historical price changes rather than implied by options 
prices. I compute it using log returns over a rolling 24-hour window, 
annualised by multiplying by √(24×252) to convert hourly volatility into an 
annual figure comparable across assets.
High realized volatility signals a turbulent market — relevant for risk 
management, position sizing, and options pricing. EUR/USD typically shows 
annualised volatility of 5-8% in calm markets, spiking during macro events 
like Fed rate decisions or geopolitical shocks

## VWAP — Volume Weighted Average Price
vwap represents the average price weighted by volume, giving more 
importance to price levels where more trading activity occurred.
Used as refernce during trading: if buying below vwap, it suggests paying less than avergae market participant.
Note: since free FX data from Yahoo Finance does not include real interbank 
volume, a constant volume is used, which reduces VWAP to a rolling mean of 
typical price.

## Momentum Signal
Momentum is the tendency of assets that have been rising to continue rising, 
and falling assets to continue falling.
When the short-term average crosses above the long-term average, it signals 
building momentum — a potential entry signal for systematic trend-following 
strategies.

## Bid-Ask Spread proxy
The bid-ask spread is the difference between the price a market maker will 
sell at (ask) and buy at (bid). It represents the cost of trading — a direct 
measure of market liquidity. Tighter spreads mean lower transaction costs and 
higher liquidity.
Note: Instead of tick-level bid/ask data, the high-low range divided by close is used in the project.
<img width="1496" height="900" alt="fx_dashboard" src="https://github.com/user-attachments/assets/3d0d49b7-2b45-4763-8115-f5b8726771ea" />
# Key Insights
Trend: EUR/USD experienced a significant appreciation from early April before moving into a sideways consolidation phase.
Volatility: Market risk was highest in late March and early April, then moderated.
Momentum: Signals shifted frequently but were predominantly positive during the strongest uptrend.
Market Conditions: The decline in the spread proxy over time suggests improving liquidity and more stable trading conditions.
