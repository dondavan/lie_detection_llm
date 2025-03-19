import streamlit as st
import time
import datetime
#import gspread
import pandas as pd 
import random
import uuid 
#from deta import Deta as Dt
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import time
import numpy as np
import os

import pages as pages


st.set_page_config(page_title="APA", page_icon="random")
#chiave = "a0x3no1k_b2trPQTiKCBh1uduRo91GU5rPwGY7DQD"
#detadb = Dt(chiave)
#db_qa = detadb.Base("Info")
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Changed to relative path
model = TFAutoModelForSeq2SeqLM.from_pretrained('../liedetectionllm')

with open("./style/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
#from google.oauth2.service_account import Credentials
#from streamlit.components.v1 import html

# Google Sheets authentication
#scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
#creds = Credentials.from_service_account_info(st.secrets["google_service_account"], scopes=scope)
#client = gspread.authorize(creds)

# Open your Google Sheet (replace "Sheet_Name" with your actual sheet name)
#sheet_1 = client.open("Database").sheet1  # Access the first sheet
#sheet_2 = client.open("Database").get_worksheet(1)  # Access the second sheet

# Function to submit data to Google Sheets
#def submit_to_sheet_1(data):
#    sheet_1.append_row(data)

#def submit_to_sheet_2(data):
#    sheet_2.append_row(data)

# Define progress bar
total_steps = 22


# Page Navigation Logic
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    pages.welcome_page()
elif st.session_state.page == 'consent':
    pages.consent_page()
elif st.session_state.page == 'instructions':
    pages.instructions_page()
elif st.session_state.page == 'specific_instructions':
    pages.specific_instructions_page()
#elif st.session_state.page == 'example':
 #   example_page()
elif st.session_state.page == 'experiment':
    pages.experiment_page()
#elif st.session_state.page == 'final_questions':
 #   final_questions()
#elif st.session_state.page == 'feedback':
 #   feedback_page()
elif st.session_state.page == 'end':
     pages.end_page()
