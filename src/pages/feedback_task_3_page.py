import streamlit as st
import pandas as pd
from utility import chatloop, load_statements
import time

st.title("Task 3: Switch the Credibility")

def feedback_page(text_container_1, text_container_2, text_container_3, text_container_4, input_container, submit_container, nav_col_1, nav_col_2,
                  current_ori_statement, current_repharsed_text):
    
    # Classification for the original statement
    ori_classification, ori_score = chatloop(frase=current_ori_statement)
    # Initial classification
    paraphrase_classfication, classfication_score = chatloop(frase=current_repharsed_text)
    
    text_container_1.markdown(f"**Original statement:** {current_ori_statement}")

    if ori_classification == "T":
        text_container_2.markdown("This statement is **true**. The credibility score is **{}%**, represented by the coloured bar below.".format(ori_score))
    elif ori_classification == "F":
        text_container_2.markdown("This statement is **false**. The credibility score is **{}%**, represented by the coloured bar below.".format(ori_score))

    text_container_3.markdown(f"**Your statement:** {current_repharsed_text}")

    if paraphrase_classfication == "T":
        text_container_4.markdown("Your statement is **true**. The credibility score is **{}%**, represented by the coloured bar below.".format(classfication_score))
    elif paraphrase_classfication == "F":
        text_container_4.markdown("Your statement is **false**. The credibility score is **{}%**, represented by the coloured bar below.".format(classfication_score))

def click_submit():
    if st.session_state.task_3_submit_count < 5:  # Check if the limit is reached
        st.session_state['current_repharsed_text'] = str(input_txt)
        st.session_state['submit_view'] = 0
        st.session_state.task_3_submit_count += 1
    else:
        st.error("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")

def click_retry():
    if st.session_state.task_3_submit_count >= 5:  # Check if the limit is reached
        st.warning("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")
    else:
        st.session_state['submit_view'] = 1

def click_next():
    st.session_state['new_statement'] = 1
    st.session_state['goto_new_statement'] = 1

# Page description
text_container_1 = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
text_container_4 = st.empty()
input_container = st.empty()
submit_container = st.empty()
nav_col1, nav_col2 = st.columns(2, gap="medium")

# states
current_ori_statement = st.session_state['current_ori_statement']
current_repharsed_text = st.session_state['current_repharsed_text']

# Display feedback
feedback_page(text_container_1, text_container_2, text_container_3, text_container_4, input_container, submit_container, nav_col1, nav_col2,
              current_ori_statement=current_ori_statement, 
              current_repharsed_text=current_repharsed_text)

# Navigation logic
if 'goto_new_statement' in st.session_state and st.session_state['goto_new_statement'] == 1:
    st.session_state['goto_new_statement'] = 0
    st.switch_page("pages/task_4_content_page.py")

if 'submit_view' in st.session_state and st.session_state['submit_view'] == 1:
    nav_col1 = st.empty()
    nav_col2 = st.empty()
    input_txt = input_container.text_area("Write your text below:")
    submit_butt = submit_container.button('Submit',on_click = click_submit)

if 'submit_view' not in st.session_state or st.session_state['submit_view'] == 0:
    retry_butt = nav_col1.button("Retry",on_click=click_retry)
    next_butt = nav_col2.button("Next",on_click=click_next)

# Display submission count
st.info(f"Submissions used: {st.session_state.task_3_submit_count}/5")