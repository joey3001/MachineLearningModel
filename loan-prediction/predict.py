import os
import settings
import pandas as pd
from sklearn import metrics
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

def cross_validate(train):
  clf = LogisticRegression(random_state=1, class_weight='balanced')

  predictors = train.columns.tolist()
  predictors = [p for p in predictors if p not in settings.NON_PREDICTORS]

  predictions = model_selection.cross_val_predict(clf, train[predictors], train[settings.TARGET], cv = settings.CV_FOLDS)
  return predictions  

def compute_error(target, predictions):
    return metrics.accuracy_score(target, predictions)

def compute_false_negatives(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0] / (df[(df["target"] == 1)].shape[0] + 1)

def compute_false_positives(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0] / (df[(df["target"] == 0)].shape[0] + 1)