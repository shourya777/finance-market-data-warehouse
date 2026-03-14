CREATE OR REPLACE TABLE `marketdataproject-490221.market_data_warehouse.stg_market_prices` AS
SELECT
  CAST(Date AS DATE) AS market_date,
  UPPER(TRIM(ticker)) AS ticker,
  CAST(close_price AS FLOAT64) AS close_price
FROM `marketdataproject-490221.market_data_warehouse.raw_market_prices`
WHERE close_price IS NOT NULL;
