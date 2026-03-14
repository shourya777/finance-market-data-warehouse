
SELECT *
FROM `marketdataproject-490221.market_data_warehouse.fct_market_prices`
WHERE market_date IS NULL
   OR asset_id IS NULL
   OR close_price IS NULL;
