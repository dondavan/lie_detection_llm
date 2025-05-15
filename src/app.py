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
experiment_intro_1_page = st.Page("pages/experiment_intro_1_page.py")
experiment_intro_2_page = st.Page("pages/experiment_intro_2_page.py")
experiment_intro_3_page = st.Page("pages/experiment_intro_3_page.py")
experiment_step_1_page = st.Page("pages/experiment_step_1_page.py")
experiment_step_2_page = st.Page("pages/experiment_step_2_page.py")
experiment_step_3_page = st.Page("pages/experiment_step_3_page.py")
feedback_page = st.Page("pages/feedback_page.py")
main_task_page = st.Page("pages/main_task_page.py")
stepwise_training_page = st.Page("pages/stepwise_training_page.py")
task_1_content_page = st.Page("pages/task_1_content_page.py")
task_2_content_page = st.Page("pages/task_2_content_page.py")
feedback_task_2_page = st.Page("pages/feedback_task_2_page.py")
task_3_content_page = st.Page("pages/task_3_content_page.py")
feedback_task_3_page = st.Page("pages/feedback_task_3_page.py")

pg = st.navigation([welcome_page,
                    consent_page,
                    instructions_page,
                    end_page,
                    experiment_intro_1_page,
                    experiment_intro_2_page,
                    experiment_intro_3_page,
                    experiment_step_1_page,
                    experiment_step_2_page,
                    experiment_step_3_page,
                    feedback_page,
                    main_task_page,
                    stepwise_training_page,
                    task_1_content_page,
                    task_2_content_page,
                    task_3_content_page,
                    feedback_task_3_page,
                    feedback_task_2_page],position = "hidden")
pg.run()

