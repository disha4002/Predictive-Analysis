# Predictive Analytics Using Historical Data — Project Report

## 1. Introduction
Predictive analytics uses historical information, statistical techniques and machine learning to estimate future outcomes. This project forecasts monthly revenue using historical sales and business variables.

## 2. Objective
The goal is to build a predictive model, evaluate its accuracy and use it to forecast future revenue trends.

## 3. Data Preparation
The dataset contains 60 monthly observations from January 2021 to December 2025. Time features, lag features and a three-month rolling revenue average were created to capture trend and recent behavior.

## 4. Modeling
A Linear Regression model was trained using the first 80% of the chronological data and tested on the final 20%. A chronological split was used instead of random splitting to avoid using future observations to predict earlier observations.

## 5. Evaluation
The test-set metrics were:
- MAE: 6,401.69
- RMSE: 7,676.19
- R²: 0.8225

MAE represents the average absolute prediction error. RMSE gives greater weight to larger errors. R² indicates the proportion of variance explained by the model on the test period.

## 6. Forecasting
A six-month forecast was generated after the historical period. Forecast values are illustrative and depend on projected business inputs.

## 7. Visualization
Power BI can be used to show historical revenue, actual vs predicted revenue, model accuracy and future forecast values.

## 8. Business Applications
The forecast can support:
- inventory planning
- marketing budget planning
- sales target setting
- staffing/capacity planning
- monitoring changes in demand

## 9. Conclusion
The project demonstrates an end-to-end predictive analytics workflow: historical data preparation, feature engineering, model training, time-aware evaluation, forecasting and business visualization.
