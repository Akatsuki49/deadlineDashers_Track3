from keyphrase_vectorizers import KeyphraseCountVectorizer
from keybert import KeyBERT
import joblib
import torch
kw_model = KeyBERT(model="paraphrase-mpnet-base-v2")
# torch.save(kw_model.state_dict(),'keybert_model.pth')
joblib.dump(kw_model, 'keybert_model.pkl')
