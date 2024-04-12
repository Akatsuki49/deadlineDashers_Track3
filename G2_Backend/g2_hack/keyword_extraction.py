import nltk
from keyphrase_vectorizers import KeyphraseCountVectorizer
from nltk.corpus import stopwords
import os
import joblib
import json
import torch
# nltk.download("stopwords")
# nltk.download('punkt')
# r=Rake()

def keygen(text):
    kw_model = joblib.load('keybert_model.pkl')
    keywords = kw_model.extract_keywords(text,top_n=20,vectorizer = KeyphraseCountVectorizer(),diversity=0.8)
    return keywords
