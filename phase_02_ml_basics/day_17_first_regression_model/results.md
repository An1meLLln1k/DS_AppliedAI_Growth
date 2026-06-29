# Day 17: First regression model

## Goal

Train and evaluate a first simple regression model.

## Task

Predict order amount using user and order-related features.

## Target

The target variable is:

amount 

Features

The model uses the following raw features:

user_age
previous_orders
is_premium
product_category
city

Categorical features were encoded with one-hot encoding using pd.get_dummies().

Model

The model used:

LinearRegression
Metrics

Results on the test set:

MAE: 4078.66
R2: 0.984
Interpretation

MAE means that the model is wrong by about 4,079 rubles on average.

R² is high on this small synthetic dataset, but the result should not be treated as reliable without a baseline and testing on a larger dataset.

Risk note

One prediction was negative, which is not valid for an order amount.

This shows that even when aggregate metrics look good, individual predictions still need business logic checks.

Key takeaway

A machine learning model should be evaluated not only by metrics, but also by checking whether its predictions make sense in the business context.