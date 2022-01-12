## Problem statement

The goal for this project is to predict how likely will a customer respond to an offer, based on demographics and offer sent data. The target variable is a boolean value that indicates if a customer is going to buy it (1) or not (0). 

It is worth noticing that the plan is to have an introduction to this matter, and such problem can be really complicated in the real world, as it can be seen in the results. This is a continuous improvement solution, and I'm aiming to provide a minimum viable product for that.

## Packages used

The following packages are used:
<ol>
    <li> <strong>pandas</strong>: python package for data analysis.
    <li> <strong>numpy</strong>: used for numerical processing.
    <li> <strong>scitkit-learn</strong>: mainstream machine learning distribution.
</ol>

## Algorithms and tools used


Target variable is supposed to be binary (`offer_completed`). From [sklearn's documentation](https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes):
>BernoulliNB implements the naive Bayes training and classification algorithms for data that is distributed according to multivariate Bernoulli distributions; i.e., there may be multiple features but each one is assumed to be a binary-valued (Bernoulli, boolean) variable.

All of our features are binary, so this makes BernoulliNB an obvious first choice. <br>

This algorithm has a smoothing parameter, called alpha, which can be varied for best fits. The main goal is to better predict low probabilities (ours is 0.2). I'll try values really close to zero for this. Wikipedia has a [really interesting story](https://en.wikipedia.org/wiki/Sunrise_problem) for the origin of the technique. <br>

Second algorithm envolves introducing a certain level of randomness to the system, then chosing based on that. That would be a [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier). From the website:

>A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

Here we're controlling the number of estimators, i.e the number of trees in the forest. The larger the better, but harder to compute. Also, [there is a ceiling for this](https://scikit-learn.org/stable/modules/ensemble.html#forest), where the model performance starts to get closer to a plateau, as described:

> In addition, note that results will stop getting significantly better beyond a critical number of trees.

I'll start with 100, then additive increasing to check on performance.

GridSearchCV is a really powerful tool that runs through a grid of parameters trying to predict the target variable. I'll use that for model tuning.

## Files in the repository
`data_wrangling.ipynb` Data preprocessing file.
`data_analysis.ipynb` File used to conduct exploratory data analysis.
`data_modeling.ipynb` File used to actually implement algorithms.

### Data Sets
Those are the files used, and their respectives, properly pre-processed (\_clean suffix).

* portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)
* profile.json - demographic data for each customer
* transcript.json - records for transactions, offers received, offers viewed, and offers completed


## Performance Metrics

The following metrics are going to be used to measure the models performance:
<ol>
    <li> <strong>Confusion matrix</strong>: the predicted variable, which is predicting if an user will respond or not to an offer, is simply binary. This way, the confusion matrix is 2x2, hence providing a clear view of how the model is going. We're trying to minimize both errors (types I and II), but prioritizing to minimize false negatives (type II). The reason for that is that is better to send an offer to a customer that won't respond than keeping one possible buying customer from actually buying. Therefore, the higher the numbers in the main diagonal, the better.
    <li> <strong>Balanced accuracy score</strong>: this is a ratio that divides the number of correct predictions versus the total predictions, considering non-normal distributions. The main target variable we're trying to predict is binary, with dataset mean on 0.2. That means it is highly unbalanced, and taking this into account would get more precision. We're aiming to get is as close as possible to 1. 
</ol>

## Tests conducted
### Random Forest
Tests were conducted from 100 to 1000 trees, in steps of 100. One characteristic to notice at this point is that overall runtime was sort of long (it took 18 minutes to run in my local machine). Balanced accuracy of 50%, and no false positives. We had around ~6.5k false negatives, which can be possible customers. This can get a little bit lower.

### Bernoulli Naive-Bayes
Using the Bernoulli Naive-Bayes led to the exact same results. Parameters tested included alpha (Laplacian smoothing) negative powers of ten from 1 to 9.
This doesn’t seem to be overfitting, but the training data might be more on the lower side. However, results seem pretty acceptable if compared to using nothing.

## Possible improvements: 
<ol>
    <li>Check how long do the customers take to respond to an offer (this might be interesting to better calibrate the expirations).
    <li>Compare amount spent versus number of offers (maybe better offers for high conversion customers).
</ol>

## Loading data

Data was cleaned in `data_modeling.ipynb`.
