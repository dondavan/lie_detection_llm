import streamlit as st
import pandas as pd
from utility import chatloop, load_statements
import time

st.title("Task 4: Switch the Credibility with Contraints")

def feedback_page(text_container_1,text_container_2,text_container_3, nav_col_2, nav_col2,
                  current_ori_statement,current_repharsed_text):

    # Initial classification
    paraphrase_classfication, classfication_score = chatloop(frase=current_repharsed_text)
    
    text_container_1.markdown(f"Original statement: {current_ori_statement}")
    text_container_2.markdown(f"Your statement: {current_repharsed_text}")

    if paraphrase_classfication == "T":
        text_container_3.markdown("Your statement is true. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(classfication_score))
    elif paraphrase_classfication == "F":
        text_container_3.markdown("Your statement is false. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(classfication_score))

def click_next():
    st.session_state['new_statement'] = 1
    st.session_state['goto_new_statement'] = 1

# Page description
text_container_1 = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
nav_col1, nav_col2 = st.columns(2, gap="medium")

# states
current_ori_statement = st.session_state['current_ori_statement']
current_repharsed_text = st.session_state['current_repharsed_text']

# Display feedback
feedback_page(text_container_1, text_container_2, text_container_3, nav_col1, nav_col2,
              current_ori_statement=current_ori_statement, 
              current_repharsed_text=current_repharsed_text)

# Navigation logic
if 'goto_new_statement' in st.session_state and st.session_state['goto_new_statement'] == 1:
    st.session_state['goto_new_statement'] = 0
    st.switch_page("pages/main_task_page.py")

# Display "Next" button
next_butt = nav_col1.button("Next", on_click=click_next)