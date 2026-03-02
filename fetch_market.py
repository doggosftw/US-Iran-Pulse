import yfinance as yf
import json
from datetime import datetime

# Fetch Brent Crude and Gold
brent = yf.ticker.Ticker("BZ=F")
gold = yf.ticker.Ticker("GC=F")

hist_brent = brent.history(start="2026-01-01", end="2026-03-02")
hist_gold = gold.history(start="2026-01-01", end="2026-03-02")

markets = []
dates = sorted(list(set(hist_brent.index.tolist() + hist_gold.index.tolist())))

for date in dates:
    brent_val = hist_brent.loc[date]['Close'] if date in hist_brent.index else None
    gold_val = hist_gold.loc[date]['Close'] if date in hist_gold.index else None
    
    # Forward fill if missing (weekends/holidays)
    if brent_val is None and len(markets) > 0:
        brent_val = markets[-1]['brent']
    if gold_val is None and len(markets) > 0:
        gold_val = markets[-1]['gold']
        
    if brent_val and gold_val:
        markets.append({
            "time": date.strftime("%Y-%m-%d"),
            "brent": round(float(brent_val), 2),
            "gold": round(float(gold_val), 2)
        })

with open("market_data.json", "w") as f:
    json.dump(markets, f, indent=2)

print("Market data saved.")
