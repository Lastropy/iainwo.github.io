It's amazing how fast time flies.
![Battle for DL](assets/images/battleForDL.png)
It's even more amazing when you haven't completely squandered it :p

Recently I was writing down what I have learned or reviewed.
The list is bigger than I remember it, but by my own opinion still pretty small.

Behold!

Review Stats Topics:
* histograms, PMF, PDF, CDF, percentiles/quartiles/other-tiles, percentile ranks, kernel density estimation
* summary statistics
    * central tendency, mean/median
    * moment statistics: mean, std, skew, kurtosis
        * raw vs central, in ref to x=0 vs centered on the avg/median
        * robustness to outliers/extreme vals
    * z-scores and effect size
* distributions
    * briefly bernoulli
    * exponential, normal, lognormal, Pareto
    * didn't really look at uniform
* relations
    * correlation vs. causation
    * covariance
    * Pearson correlation/spearman's rank correlation
    * briefly at non-linear relationships graphed in 2d
* estimation
    * estimation process and estimators
        * sample mean, sample std
        * mean squared error and rmse
        * very briefly MLE
        * biased vs unbiased estimators
            * bias(theta-hat) = expectation(theta-hat) - theta
            * variance(theta-hat) = mse(theta-hat) - bias(theta-hat)**2
            * asymptotically unbiased estimators
            * relative efficiency, eff(theta-hat-1, theta-hat-2): var(theta-hat-2)/var(theta-hat-1) > 1
        * concepts of sampling bias, self selection, measurement error briefly
* hypothesis testing
    * null-hypothesis
    * chi-squared
    * correlation and p-values briefly - kind of shaky on this
* linear least squares
    * briefly
        * gramian matrix
        * single value decomp
            * then use derivatives and matrix-calc to find the params
            * don't use analytical math - instead use gradient descent
* models
    * decision trees briefly
    * random forests briefly
    * handling missing numerical and categorical data
        * dropping rows/cols
        * imputing values (univariate)
            * mean/median, constant val for categorical/numer,
        * imputing and augmenting with features describing if the value was imputed
    * categorical
        * labelling
        * labelling with intended ordinal assignment
        * one hot encoding for categories with less than 15 vals
    * under/overfitting
        * splitting data in train/validation/test data
        * using cross validation
            * divide all data into segments, then use each segment as a validation data set and the rest as training data and determine best model which generalizes across all combinations
* exploratory data analysis
    * plotting
        * box plots
        * I've seen violinplots but don't really understand them

For some reason - probably because I've been doing a bit of Kaggle, i've been thinking about kernels.
Well look at that kernel of knowledge ^^^. Ya lame - I agreeeeee.

TODO: add kaggle profile to the Daily Distribution

Best,
Iain
