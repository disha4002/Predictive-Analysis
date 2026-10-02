# Power BI Dashboard Guide

## Dashboard Title
Revenue Forecasting & Predictive Analytics

## Page 1 — Historical Performance
KPI Cards:
- Total Revenue
- Total Orders
- Average Order Value
- Average Monthly Revenue

Visuals:
1. Line chart — Date vs Revenue
2. Column chart — Monthly Orders
3. Line/column chart — Revenue and Marketing Spend
4. Line chart — Average Order Value over time
5. Slicers — Year and Month

## Page 2 — Model Evaluation
Use `test_predictions.csv`.

Visuals:
1. Line chart — Actual Revenue vs Predicted Revenue
2. KPI — MAE
3. KPI — RMSE
4. KPI — R²
5. Table — Date, Actual Revenue, Predicted Revenue, Absolute Error

## Page 3 — Future Forecast
Use `six_month_forecast.csv`.

Visuals:
1. Line chart — Forecast Revenue by Date
2. Column chart — Projected Orders
3. Card — Average Forecast Revenue
4. Table — Month, Forecast Revenue, Projected Orders, Projected AOV

## Suggested business insights
- Use the forecast to support sales and inventory planning.
- Compare forecasted demand with operational capacity.
- Use seasonal patterns to plan campaigns.
- Track forecast error regularly and retrain the model when new actual data becomes available.

## DAX examples
Total Revenue = SUM(historical_sales_data[Revenue])

Total Orders = SUM(historical_sales_data[Orders])

Average Order Value = DIVIDE([Total Revenue], [Total Orders])

Forecast Revenue = SUM(six_month_forecast[Forecast_Revenue])
