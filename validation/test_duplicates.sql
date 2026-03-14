SELECT
  market_date,
  asset_id,
  COUNT(*) AS row_count
FROM `marketdataproject-490221.market_data_warehouse.fct_market_prices`
GROUP BY market_date, asset_id
HAVING COUNT(*) > 1;
