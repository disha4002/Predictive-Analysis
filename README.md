# Predictive Analytics Using Historical Data

## Objective
Build a predictive model using historical business data to forecast future revenue trends.

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Power BI

## Dataset
This project uses 60 months of synthetic monthly sales history from January 2021 to December 2025.

Variables include:
- Date
- Orders
- Average Order Value
- Marketing Spend
- Revenue

## Methodology
1. Load and inspect historical data.
2. Create time-based features.
3. Create lag and rolling-average features.
4. Split the data chronologically into training and testing sets.
5. Train a Linear Regression model.
6. Evaluate predictions using MAE, RMSE and R².
7. Generate a six-month revenue forecast.
8. Visualize historical vs predicted revenue in Power BI.

## Model Performance
The model was evaluated on the final 20% of the time series.

- MAE: 6,401.69
- RMSE: 7,676.19
- R²: 0.8225

## Files
- `historical_sales_data.csv` — original historical dataset
- `model_ready_data.csv` — engineered dataset
- `test_predictions.csv` — actual vs predicted test period
- `six_month_forecast.csv` — six-month future forecast
- `model_metrics.csv` — evaluation metrics
- `predictive_analytics.py` — reproducible modeling script
- `powerbi_dashboard_guide.md` — dashboard instructions
- `project_report.md` — project report

## Business Questions
- What is the historical revenue trend?
- How accurately can revenue be predicted?
- Which months show seasonal patterns?
- What could revenue look like over the next six months?
- How can forecasts support inventory, marketing and sales planning?

## Important Note
The dataset is synthetic and created for an academic/internship project. Forecasts are illustrative and should be validated against real business data before operational decisions.
