from deta import Deta as Dt
import streamlit as st
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import time
import numpy as np
import os
import pandas as pd


st.set_page_config(page_title="VLD", page_icon="random")
chiave = "a0x3no1k_b2trPQTiKCBh1uduRo91GU5rPwGY7DQD"
detadb = Dt(chiave)
db_qa = detadb.Base("Info")
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSeq2SeqLM.from_pretrained(r'./liedetectionllm')

with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title("LLM based Verbal Lie Detection")
st.markdown("Instructions for use:") 
st.markdown("▶  Write a short story which can either be true or false.")
st.markdown("▶  The system will attempt to evaluate the truthfulness of the input, by giving a credibility score (probability).")
obj = '<p style="color:#06b0db; font-size: 20px; fond-weight: bold;">Try to fool the system by finding an adversarial example</p>'
st.markdown(obj, unsafe_allow_html=True)
desc = st.markdown("Write your text below:")
col1, col2 = st.columns([3,1])
col3, col4 = st.columns([5,1])

ans_container = st.empty()
input_container = col1.empty()
submit_cont = col2.empty()
progr_cont = st.empty()
up_button_cont = col4.empty()
down_button_cont = col3.empty()


def store(domanda, risposta, feedback, ind):
    database = pd.read_csv("./database.csv")
    try:
        database = database.drop(['Unnamed: 0'], axis=1)
    except:
        pass
    if feedback:
        correttezza = "Corretto"
    elif feedback== False:
        correttezza = "Sbagliato"
    row = pd.DataFrame.from_records({"Index": ind, "Domanda": domanda, "Risposta": risposta, "Feedback": correttezza}, index=[0])
    database = pd.concat([database,row ], ignore_index=True)
    
    database.to_csv('./database.csv')
    
    load(j=ind)

def chatloop(frase):
    tokenize = tokenizer(frase, return_tensors='tf')
    for i in [tokenize]:
        h = model.generate(**i)
        decoded_pred = tokenizer.batch_decode(h, skip_special_tokens=True)
        h1 = model.generate(**i, return_dict_in_generate=True, output_scores=True)
        prob = np.max(np.exp(h1.scores)/np.sum(np.exp(h1.scores)))
    return decoded_pred[0], prob

def generate(input_txt, index):
    risposta, sicurezza = chatloop(frase=str(input_txt))
    prob = str(sicurezza)[2] + str(sicurezza)[3]
    prob = int(prob)
    submit_cont.empty()
    input_container.empty()
    if risposta == "T":
        desc.markdown("The paragraph is true. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(prob))
        up_button = up_button_cont.button("CORRECT", key=index+500, on_click=store, args=(input_txt,risposta,True,index))
        down_button = down_button_cont.button("WRONG", key=-(index + 500), on_click=store, args=(input_txt, risposta, False, index))
        progr_cont.progress(prob)
    elif risposta == "F":
        desc.markdown("The paragraph is false. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(prob))
        up_button = up_button_cont.button("CORRECT", key=(index+5)*500, on_click=store, args=(input_txt, risposta, True, index))
        down_button = down_button_cont.button("WRONG", key=-(index+5)*500, on_click=store, args=(input_txt, risposta, False, index))
        progr_cont.progress(prob)
    elif risposta == "recalled":
        warn = st.warning("I didn't understand, please try again. Reloading...")
        time.sleep(3)
        warn.empty()
        load(j=index)

def load(j):
    j+=1
    input_container.empty()
    progr_cont.empty()
    ans_container.empty()
    up_button_cont.empty()
    down_button_cont.empty()
    input = input_container.text_area("",key=j, label_visibility="collapsed")
    submit_butt = submit_cont.button("SUBMIT", key=-j)
    if submit_butt:
        generate(input, j)

load(j=0)
for i in range (0,8):
    st.text("")

st.markdown("""NOTE:""")
st.markdown("♠ The LLM-based verbal lie detector is based on the Flan T5 large language model: https://huggingface.co/google/flan-t5-base")
st.markdown("♠ It has been trained on open sourced datasets of autobiographical memories, beliefs and intentions.")
st.markdown("♠ The feedback you provide through the use of this page will be used to further fine tune the model with adversarial examples.")