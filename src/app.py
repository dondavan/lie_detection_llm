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

with open("./style/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


welcome_page = st.Page("pages/welcome_page.py")
consent_page = st.Page("pages/consent_page.py")
instructions_page = st.Page("pages/instructions_page.py")
end_page = st.Page("pages/end_page.py")
experiment_intro_page = st.Page("pages/experiment_intro_page.py")
experiment_step_page = st.Page("pages/experiment_step_page.py")
feedback_page = st.Page("pages/feedback_page.py")
specific_instructions_page = st.Page("pages/specific_instructions_page.py")
stepwise_training_page = st.Page("pages/stepwise_training_page.py")
task_1_content_page = st.Page("pages/task_1_content_page.py")
task_2_content_page = st.Page("pages/task_2_content_page.py")

pg = st.navigation([welcome_page,
                    consent_page,
                    instructions_page,
                    end_page,
                    experiment_intro_page,
                    experiment_step_page,
                    feedback_page,
                    specific_instructions_page,
                    stepwise_training_page,
                    task_1_content_page,
                    task_2_content_page],position = "hidden")
pg.run()

