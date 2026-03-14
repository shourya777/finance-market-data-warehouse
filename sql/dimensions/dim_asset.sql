
CREATE OR REPLACE TABLE `marketdataproject-490221.market_data_warehouse.dim_asset` AS
SELECT DISTINCT
  ticker AS asset_id,
  ticker AS ticker,
  CASE
    WHEN ticker IN ('AAPL', 'MSFT') THEN 'Technology'
    WHEN ticker IN ('JPM', 'GS') THEN 'Financials'
    ELSE 'Other'
  END AS sector
FROM `marketdataproject-490221.market_data_warehouse.stg_market_prices`;
