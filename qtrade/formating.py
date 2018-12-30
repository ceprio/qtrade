import pandas as pd

def simplify_quote(results):
    df = pd.DataFrame(results)
    df = df.drop(columns=["symbolId", "lastTradePriceTrHrs", "lastTradeSize", "lastTradeTime", "isHalted", "VWAP", "askPrice", "askSize",
                    "bidPrice", "bidSize", "delay", "tier", "volume"])
    return df
