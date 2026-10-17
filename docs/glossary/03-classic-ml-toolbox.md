# 3. Classic ML toolbox

*Pre-deep-learning algorithms and the vocabulary of any ML project*

Still the right tool for most tabular business data. The evaluation vocabulary here (train/test split, overfitting, hyperparameters) applies to LLMs too.

!!! info "How to read this section"
    Each entry is a short definition followed by a **Why it matters** line that says, in plain words, what the idea buys you. Terms marked ★ belong to the [30 to learn first](../index.md#learn-these-30-first). The **Also known as** line lists the acronyms and other names you may hear in videos; all of them appear in the [A–Z index](../index-a-z.md).

### Linear regression { #linear-regression }

Fit a straight line (or hyperplane) to predict a number.

**Why it matters:** The simplest model there is; everything else is a more flexible version of "fit a curve to the data".

### Logistic regression { #logistic-regression }

A linear model for classification that outputs a probability.

**Why it matters:** Fast, explainable baseline. If a neural network cannot beat it, something is wrong.

<small>*Index aliases:* Logistic regression (classifier)</small>

### Decision tree { #decision-tree }

A flowchart of if/else splits on features. Easy to read, prone to overfitting.

**Why it matters:** Humans can read the rules it learned, which makes it popular where decisions must be explained.

<small>*Index aliases:* Decision trees</small>

### Random forest { #random-forest }

Many decision trees trained on random subsets of data and features, then averaged.

**Why it matters:** Averaging many imperfect trees cancels their individual mistakes: more accurate and far more robust than one tree.

<small>*Index aliases:* Random forest (ensemble)</small>

### Gradient boosting { #gradient-boosting }

*Also known as:* XGBoost, LightGBM, CatBoost

Build trees one after another, each correcting the errors of the previous ones.

**Why it matters:** The most accurate choice for tabular data in most competitions and companies. Try this before a neural network.

<small>*Index aliases:* Gradient boosting (XGBoost, LightGBM)</small>

### Support Vector Machine (SVM) { #support-vector-machine }

Finds the boundary with the widest margin between classes.

**Why it matters:** A strong pre-2012 classifier; a wide margin makes it generalise well on small datasets.

<small>*Index aliases:* SVM</small>

### k-Nearest Neighbours (kNN) { #k-nearest-neighbours }

Predict by looking at the k most similar training examples.

**Why it matters:** No training at all, just lookup. The same idea powers vector search in RAG: find the nearest embeddings.

<small>*Index aliases:* kNN</small>

### Naive Bayes { #naive-bayes }

Fast probabilistic classifier that assumes features are independent.

**Why it matters:** The classic spam filter; works surprisingly well on text with almost no compute.

<small>*Index aliases:* Naive Bayes classifier</small>

### k-means { #k-means }

Clustering by assigning points to the nearest of k centroids and repeating until stable.

**Why it matters:** The default way to split data into k groups when you have no labels.

### Principal Component Analysis (PCA) { #principal-component-analysis }

Linear dimensionality reduction along the directions of largest variance.

**Why it matters:** Compresses data while keeping what varies most; used to shrink embeddings and to visualise them.

<small>*Index aliases:* PCA</small>

### Feature / feature engineering { #feature-feature-engineering }

A feature is one input variable. Feature engineering is hand-crafting better inputs.

**Why it matters:** In classic ML, good features matter more than the algorithm. Deep learning's big win is learning features automatically.

<small>*Index aliases:* Feature engineering</small>

### Train / validation / test split { #train-validation-test-split }

Data is divided so you train on one part, tune settings on a second and measure final performance on a third the model never saw.

**Why it matters:** The only honest way to know how a model will do on new data. Skipping it is how projects fool themselves.

<small>*Index aliases:* Validation set, Test set</small>

### Cross-validation { #cross-validation }

Rotate which slice is held out and average, for a more reliable estimate.

**Why it matters:** Gives a trustworthy accuracy number from a small dataset.

### Overfitting / underfitting ★ { #overfitting-underfitting }

Memorising the training data (great on train, poor on new data) versus being too simple to capture the pattern at all.

**Why it matters:** Overfitting is the number-one way models fail in production: perfect in the lab, useless on real inputs.

### Bias–variance trade-off { #biasvariance-trade-off }

Simple models err systematically (bias); complex models err erratically depending on the data they saw (variance).

**Why it matters:** Explains why bigger is not always better: a model can be too flexible for the amount of data you have.

<small>*Index aliases:* Bias–variance</small>

### Regularization { #regularization }

*Also known as:* L1, L2

Penalising large weights to reduce overfitting. L1 also pushes weights to exactly zero.

**Why it matters:** Makes a model generalise better by stopping it from relying too hard on any one input.

<small>*Index aliases:* L1 / L2 regularization</small>

### Early stopping { #early-stopping }

Stop training when validation loss stops improving, even if training loss is still falling.

**Why it matters:** The cheapest protection against overfitting: just stop at the right moment.

### Hyperparameter { #hyperparameter }

A setting you choose before training (learning rate, tree depth, LoRA rank), as opposed to parameters learned from data.

**Why it matters:** What engineers tune by hand; a wrong learning rate can make an otherwise good model fail completely.

### Ensemble { #ensemble }

Combining several models' predictions.

**Why it matters:** Usually beats any single model; the same idea as asking several experts and taking the majority view.

### Confusion matrix { #confusion-matrix }

A table of predicted class versus actual class, showing where a classifier confuses things.

**Why it matters:** Shows which mistakes the model makes, not just how many. Essential when some errors cost more than others.

### Precision, recall, F1, ROC / AUC { #precision-recall-f1-roc-auc }

Precision: of what the model flagged, how much was right. Recall: of what should be flagged, how much it caught. F1 balances the two; ROC / AUC summarises the trade-off across thresholds.

**Why it matters:** Accuracy alone lies when classes are unbalanced (99% "not fraud" is 99% accurate and useless). These metrics tell the truth.

<small>*Index aliases:* AUC / ROC, Precision / recall, F1 score</small>

### Data leakage { #data-leakage }

Information from the test set, or from the future, accidentally reaching the training data.

**Why it matters:** The classic reason a model scores brilliantly in testing and fails in production.

### Class imbalance { #class-imbalance }

When one class is far rarer than the other (fraud, defects, disease).

**Why it matters:** Needs special handling (re-weighting, re-sampling, the right metrics) or the model simply learns to predict the majority class.

### scikit-learn { #scikit-learn }

The standard Python library for classic ML.

**Why it matters:** Where almost every tutorial's `.fit()` and `.predict()` come from.
