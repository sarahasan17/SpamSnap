import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

vectorizer = joblib.load('vectorizer.joblib')

def predict(data):
    trans = vectorizer.transform(pd.DataFrame(data)[0])
    clf = joblib.load('model.sav')

    return clf.predict(trans)
