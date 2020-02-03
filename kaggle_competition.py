# -*- coding: utf-8 -*-
"""kaggle_Competition

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZ76eYvc9MfT4RBrc5AfF1RYIC2rwi90
"""

import pandas as pd
import numpy as np
from sklearn import feature_extraction,linear_model,model_selection,preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer

train = pd.read_csv("/content/train.csv")
test = pd.read_csv("/content/test.csv")
train.head()

train.isnull().sum()
train[train['target']==0]['text'].values[1]
train[train['target']==1]['text'].values[1]
x = train['text']
y = train['target']

vectorizer = TfidfVectorizer()
xtrain_tfidf = vectorizer.fit_transform(x)

from sklearn.svm import LinearSVC
clf = LinearSVC()
clf.fit(train_idf,y)


from sklearn import model_selection
scores = model_selection.cross_val_score(clf,train_idf,train['target'],cv=3,scoring='f1')
scores
