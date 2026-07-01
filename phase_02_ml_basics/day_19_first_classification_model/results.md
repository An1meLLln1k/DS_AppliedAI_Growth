# Day 19: First classification model

## Goal

Train and evaluate a first binary classification model.

## Task

Predict whether an order is a high-value order.

## Target

The target variable is:

```text
high_value_order
```

Target logic:

```text
1 = amount >= 50000
0 = amount < 50000
```

## Features

The model uses the following raw features:

* `user_age`
* `previous_orders`
* `is_premium`
* `product_category`
* `city`

The `amount` column is excluded from features to avoid target leakage, because the target is created directly from `amount`.

Categorical features were encoded with one-hot encoding using `pd.get_dummies()`.

## Baseline

The baseline predicts the majority class from the training set for every test example.

In this case, the majority class is:

```text
0
```

This means the baseline always predicts that an order is not high-value.

## Model

The classification model used:

```text
LogisticRegression
```

## Metrics comparison

```text
Baseline accuracy: 0.6
Baseline precision: 0.0
Baseline recall: 0.0
Baseline F1: 0.0

Model accuracy: 0.8
Model precision: 1.0
Model recall: 0.5
Model F1: 0.667
```

## Confusion matrix

```text
[[3 0]
 [1 1]]
```

Interpretation:

* TN = 3: regular orders correctly predicted as regular;
* FP = 0: no regular orders incorrectly predicted as high-value;
* FN = 1: one high-value order was missed;
* TP = 1: one high-value order was correctly detected.

## Interpretation

The logistic regression model performed better than the majority-class baseline by F1 score.

The baseline did not detect any high-value orders. The model detected one high-value order and made no false positive predictions.

However, recall is only 0.5, which means the model missed one of two real high-value orders in the test set.

## Risk note

The model is precise but conservative.

High precision means that when the model predicts a high-value order, it is reliable in this test split. Low recall means that some high-value orders may be missed.

For a high-value detection task, recall may be more important if missing important orders is costly.

## Key takeaway

Classification models should not be evaluated only by accuracy.

Precision, recall, F1 score and the confusion matrix help explain what types of errors the model makes.
