
CREATE OR REPLACE TABLE `marketdataproject-490221.market_data_warehouse.fct_market_prices` AS
SELECT
  market_date,
  ticker AS asset_id,
  close_price
FROM `marketdataproject-490221.market_data_warehouse.stg_market_prices`;
