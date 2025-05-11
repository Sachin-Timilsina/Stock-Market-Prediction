from investiny import search_assets, historical_data
import pandas as pd
from datetime import datetime

# Search for Apple ID in investing.com
results = search_assets(query="Apple", limit=5)
investing_id = results[0]['ticker'] # Ticker ID of APPL

# Date range for historical data
data = historical_data(
    investing_id=investing_id,
    from_date="05/09/2020 00:00",
    to_date="05/09/2025 00:00",
)

df = pd.DataFrame(data)
df.to_csv("apple_stock_data.csv", index=False)