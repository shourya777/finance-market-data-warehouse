# Data Model Documentation

## dim_asset
**Description:** Asset reference table containing metadata for each traded asset.

**Grain:** One row per asset (ticker)

| Column | Description |
|------|-------------|
| asset_id | Unique identifier for asset |
| ticker | Stock ticker symbol |
| sector | Industry sector classification |

---

## fct_market_prices
**Description:** Fact table containing daily market price observations.

**Grain:** One row per asset per day

| Column | Description |
|------|-------------|
| market_date | Trading date |
| asset_id | Asset identifier |
| close_price | Daily closing price |

---

## kpi_daily_return
**Description:** Calculates daily percentage return for each asset.

| Column | Description |
|------|-------------|
| market_date | Trading date |
| asset_id | Asset identifier |
| previous_close_price | Previous day's closing price |
| daily_return | Percentage change from previous close |

---

## kpi_moving_average
**Description:** Calculates 7-day moving average for asset prices.

| Column | Description |
|------|-------------|
| market_date | Trading date |
| asset_id | Asset identifier |
| close_price | Daily closing price |
| moving_avg_7d | 7-day rolling average price |
