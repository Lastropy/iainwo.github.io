Kind of got burnt out the last week doing stats and it's mathemtatics.

![One hot encoding](https://i.imgur.com/TW5m0aJ.png)

Rather than taking a break from things, I wanted to still keep productive.

Instead I've alternated to doing some lessons on Kaggle.

So far I've started two courses,

1. [Machine Learning Micro-Course Home Page](https://www.kaggle.com/learn/intro-to-machine-learning) 
2. [Intermediate Machine Learning Micro-Course Home Page](https://www.kaggle.com/learn/intermediate-machine-learning)

And have read about the rudiments of,

1. Decision Trees
2. Random Forest Regression
3. Model Parameters
  1. Number of estimators used in a Random Forest
4. Handling missing data
  1. Dropping rows/cols
  2. Imputing data
  3. Imputing data and generating metadata (adding extra cols, is imputed/not)
5. Handling categorical data
  1. Dropping rows/cols
  2. Labeling
    1. Ordinal vs. Nominal?      
  3. One Hot Encoding
    1. Best when number of categories < 15

I even entered a kaggle competition (although it was part of the tutorial)!
Here is a sample of how I used OneHot encoding to better predict the sales of housing prices,

```python
# Remove rows with missing target, remove target column from predictors
if 'SalePrice' in X_test.columns:
    X_test.dropna(axis=0, subset=['SalePrice'], inplace=True)
    X_test.drop(['SalePrice'], axis=1, inplace=True)

X_test_null_cols = [col for col in X_test.columns if X_test[col].isnull().any()]
X_test.drop(X_test_null_cols, axis=1, inplace=True)
X_train.drop(X_test_null_cols, axis=1, inplace=True)

X_diff_train = list(set(
            set([col for col in X_train.columns if X_train[col].isnull().any()])
            .union(set([col for col in X_train.columns if col not in X_test.columns]))))
X_diff_test = list(set(
            set([col for col in X_test.columns if X_test[col].isnull().any()])
            .union(set([col for col in X_test.columns if X_test[col].isnull().any()]))))

X_train.drop(X_diff_train, axis=1, inplace=True)
X_test.drop(X_diff_test, axis=1, inplace=True)

# Get valid OneHot and LabelEncoding columns
cat_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

submit_lowcard_cols  = [col for col in cat_cols if X_train[col].nunique() < 10]
submit_highcard_cols = list(set(object_cols) - set(submit_lowcard_cols))

# Augment the training data and the test data
submit_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
submit_cols_train = pd.DataFrame(submit_encoder.fit_transform(X_train[submit_lowcard_cols])) # encode the categorical columns into OH cols
submit_cols_test  = pd.DataFrame(submit_encoder.transform(X_test[submit_lowcard_cols]))

submit_cols_train.index = X_train[submit_lowcard_cols].index # demarcate the columns
submit_cols_test.index  = X_test[submit_lowcard_cols].index

submit_num_train = X_train.drop(cat_cols, axis=1) # drop the categorical columns
submit_num_test  = X_test.drop(cat_cols, axis=1)

submit_X_train = pd.concat([submit_num_train, submit_cols_train], axis=1)
submit_X_test  = pd.concat([submit_num_test, submit_cols_test], axis=1)

model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(submit_X_train, y_train)

# Get test predictions
submit_preds = model.predict(submit_X_test)

# Save test predictions to file
output = pd.DataFrame({'Id': submit_X_test.index,
                       'SalePrice': submit_preds})
output.to_csv('submission.csv', index=False)
```

Till next time,
- Iain
