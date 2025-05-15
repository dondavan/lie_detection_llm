import streamlit as st
import time
import datetime
#import gspread
import pandas as pd 
import random
import uuid 
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer, DistilBertModel, AutoModelForSequenceClassification
from safetensors.torch import load_file
import time
import numpy as np
import os
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

#models and tokenizer
tokenizer = AutoTokenizer.from_pretrained('models/fine_tuned_model')
#model = load_file('models/fine_tuned_model/model.safetensors')
model = AutoModelForSequenceClassification.from_pretrained('models/fine_tuned_model', use_safetensors=True)

def chatloop(frase):
    """
    Process the input statement using the model and return the prediction and confidence score.
    """
     # Tokenize the text and convert to input IDs
    inputs = tokenizer(frase, return_tensors="pt")

    # Get logits, predicted probabilities, and predicted label
    outputs = model(**inputs)
    probabilities = outputs.logits.softmax(dim=-1)  
    predicted_label = probabilities.argmax().item()

    # Get the class probability 
    class_prob = probabilities[0, predicted_label].item()
    return 1-predicted_label, class_prob*100

    """
    tokenize = tokenizer(frase, return_tensors='tf')
    for i in [tokenize]:
        h = model.generate(**i)
        decoded_pred = tokenizer.batch_decode(h, skip_special_tokens=True)
        h1 = model.generate(**i, return_dict_in_generate=True, output_scores=True)
        prob = np.max(np.exp(h1.scores) / np.sum(np.exp(h1.scores))) * 100  # Convert to percentage
    return decoded_pred[0], prob
    """


def load_statements():
    with open("data/count.txt", "r+") as f:
        #go to last line
        for line in f:
            pass
        last_line = line

        count = last_line
        count= int(float(count))
        count = count + 1
        f.write(str(count)+'\n')
        f.close()
        return pd.read_csv("data/hippocorpus_test_truncated.csv", sep=",").iloc[count]
    
def reset_statement_count():
    with open("data/count.txt", "w") as f:
        f.write('0'+'\n')
        f.close()

def load_statements_2():
    return pd.read_csv("data/hippocorpus_training_truncated.csv", sep=",")


connector = Connector()


def getconn():
    conn = connector.connect(
        "paraphrasing-attacks:europe-west4:paraphraseluca", # Cloud SQL Instance Connection Name
        "pymysql",
        user="paraphraseluca",
        password="papihugh",
        db="demo",
        ip_type=IPTypes.PUBLIC # IPTypes.PRIVATE for private IP
    )
    return conn

def insert_to_sql(parameters):

    pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
    )

    '''
    pool = sqlalchemy.create_engine(
    "mysql+pymysql://paraphraseluca:papihugh@34.13.217.210:3306/demo",
    creator=getconn,
    )
    '''
    with pool.connect() as db_conn:
        # insert data into our ratings table
        insert_stmt = sqlalchemy.text(
            "INSERT INTO testing_table_time (pid, os_id, os, os_c, os_cp, paras, paras_c, paras_cp, start_time, end_time) "
            "VALUES (:pid, :os_id, :os, :os_c, :os_cp, :paras, :paras_c, :paras_cp, :start_time, :end_time)",
        )

        # insert entries into table
        db_conn.execute(insert_stmt, parameters=parameters)

        # commit transactions
        db_conn.commit()