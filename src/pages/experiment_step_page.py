import streamlit as st
import pandas as pd
from utility import chatloop, load_statements
import time

st.title("LLM based Verbal Lie Detection")
 
def feedback_page(text_container_1,text_container_2,text_container_3,input_container,submit_container,nav_col1, nav_col2,
                  current_ori_statement,current_repharsed_text):

    # Initial classification
    paraphrase_classfication, classfication_score = chatloop(frase=current_repharsed_text)
    
    text_container_1.markdown(f"Original statement: {current_ori_statement}")
    text_container_2.markdown(f"Your statement: {current_repharsed_text}")

    if paraphrase_classfication == "T":
        text_container_3.markdown("Your statement is true. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(classfication_score))
    elif paraphrase_classfication == "F":
        text_container_3.markdown("Your statement is false. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(classfication_score))

def click_submit():
    st.session_state['current_repharsed_text'] = str(input_txt)
    st.session_state['submit_view'] = 0

def click_retry():
    st.session_state['submit_view'] = 1

def click_next():
    st.session_state['new_statement'] = 1
    st.session_state['goto_new_statement'] = 1


# Page description
text_container_1 = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
input_container = st.empty()
submit_container = st.empty()
nav_col1, nav_col2 = st.columns(2,gap="medium")

# States
current_ori_statement = st.session_state['current_ori_statement']
current_repharsed_text = st.session_state['current_repharsed_text']

# Display
feedback_page(text_container_1,text_container_2,text_container_3,input_container,submit_container,nav_col1,nav_col2,
                current_ori_statement = current_ori_statement,
                current_repharsed_text = current_repharsed_text)

if 'goto_new_statement' in st.session_state and st.session_state['goto_new_statement'] == 1:
    st.session_state['goto_new_statement'] = 0
    st.switch_page("pages/experiment_intro_page.py")

if 'submit_view' in st.session_state and st.session_state['submit_view'] == 1:
    nav_col1 = st.empty()
    nav_col2 = st.empty()
    input_txt = input_container.text_area("Write your text below:")
    submit_butt = submit_container.button('Submit',on_click = click_submit)

if 'submit_view' not in st.session_state or st.session_state['submit_view'] == 0:
    retry_butt = nav_col1.button("Retry",on_click=click_retry)
    next_butt = nav_col2.button("Next",on_click=click_next)