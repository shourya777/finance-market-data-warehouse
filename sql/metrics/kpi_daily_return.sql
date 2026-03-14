
CREATE OR REPLACE TABLE `marketdataproject-490221.market_data_warehouse.kpi_daily_return` AS
SELECT
  market_date,
  asset_id,
  close_price,
  LAG(close_price) OVER (
    PARTITION BY asset_id
    ORDER BY market_date
  ) AS previous_close_price,
  SAFE_DIVIDE(
    close_price - LAG(close_price) OVER (
      PARTITION BY asset_id
      ORDER BY market_date
    ),
    LAG(close_price) OVER (
      PARTITION BY asset_id
      ORDER BY market_date
    )
  ) AS daily_return
FROM `marketdataproject-490221.market_data_warehouse.fct_market_prices`;
