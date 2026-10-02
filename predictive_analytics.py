# Predictive Analytics Using Historical Data
# Forecasting monthly revenue using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("historical_sales_data.csv", parse_dates=["Date"])

df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
df["Time_Index"] = range(len(df))
df["Revenue_Lag_1"] = df["Revenue"].shift(1)
df["Revenue_Lag_12"] = df["Revenue"].shift(12)
df["Revenue_Rolling_3"] = df["Revenue"].rolling(3).mean()

df = df.dropna().reset_index(drop=True)

features = ['Orders', 'Average_Order_Value', 'Marketing_Spend', 'Month', 'Year', 'Time_Index', 'Revenue_Lag_1', 'Revenue_Lag_12', 'Revenue_Rolling_3']
X = df[features]
y = df["Revenue"]

split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)
