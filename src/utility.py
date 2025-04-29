import streamlit as st
import time
import datetime
#import gspread
import pandas as pd 
import random
import uuid 
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import time
import numpy as np
import os

#models and tokenizer
tokenizer = AutoTokenizer.from_pretrained('models/flan')
model = TFAutoModelForSeq2SeqLM.from_pretrained('models/liedetectionllm')

def chatloop(frase):
    """
    Process the input statement using the model and return the prediction and confidence score.
    """
    tokenize = tokenizer(frase, return_tensors='tf')
    for i in [tokenize]:
        h = model.generate(**i)
        decoded_pred = tokenizer.batch_decode(h, skip_special_tokens=True)
        h1 = model.generate(**i, return_dict_in_generate=True, output_scores=True)
        prob = np.max(np.exp(h1.scores) / np.sum(np.exp(h1.scores))) * 100  # Convert to percentage
    return decoded_pred[0], prob


def load_statements():
    return pd.read_csv("data/hippocorpus_test_truncated.csv", sep=",")

def load_statements_2():
    return pd.read_csv("data/hippocorpus_training_truncated.csv", sep=",")