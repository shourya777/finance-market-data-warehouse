 Data Warehouse Architecture

Market Data Source (Yahoo Finance)
           │
           ▼
    Python Ingestion Script
           │
           ▼
     Raw Data Layer
   raw_market_prices
           │
           ▼
      Staging Layer
    stg_market_prices
           │
           ▼
   Dimension Tables
        dim_asset
           │
           ▼
       Fact Table
    fct_market_prices
           │
           ▼
       KPI Layer
   daily_return
   moving_average
           │
           ▼
   Analyst Reporting View
  vw_market_performance
