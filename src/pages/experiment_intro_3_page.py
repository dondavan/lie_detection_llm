import streamlit as st
import pandas as pd
from utility import chatloop, load_statements
import datetime

st.title("Main Task")

def load_instruction(text_container_1, feedback_container, progr_cont, text_container_2, text_container_3, text_container_4, input_container, submit_container, paraphrase_classification="X", classification_score=-1):
    # Display the statement and instructions
    if st.session_state['current_ori_statement_condition'] == "truthful":
        condition_1 = "truthful"
        condition_2 = "deceptive"
    else:
        condition_1 = "deceptive"
        condition_2 = "truthful"

    text_container_1.markdown(f"**Original statement:** {st.session_state['current_ori_statement']}")
   
    feedback_container.markdown(
        f"The AI classifies this statement as **{'TRUTHFUL' if paraphrase_classification == 1 else 'DECEPTIVE'}**.\n"
        f"Confidence Score: **{classification_score:.2f}%**"
    )
    progr_cont.progress(int(classification_score))  # Display progress bar for credibility score

    opposite_classification = 'DECEPTIVE' if paraphrase_classification == 1 else 'TRUTHFUL'
    text_container_2.markdown(
        f"Rewrite this statement so that it appears **{opposite_classification}** to the AI.\n"
        "Please maintain the statements **original meaning**, ensure that it is **grammatically correct**, and appears **natural**. A **natural** statement is coherent, fluent and readable.\n"
        "You have 10 attempts to rewrite. If you manage to flip the class (truthful to deceptive or deceptive to truthful) before that, please proceed to the next page.")
    original_tokens = len(st.session_state['current_ori_statement'].split())
    text_container_3.markdown(f"Your rewritten statement must be within 20 words of the original statement's length **(i.e., {original_tokens} +/- 20 words)**.")
    text_container_4.markdown(f"**IMPORTANT:** If the page does not respond, press submit again. DO NOT REFRESH THE PAGE.")

    st.session_state['new_statement'] = 0

def goto_exp_step():
    if not input_txt.strip():  # Check if the input is empty
        st.warning("Please write a statement before submitting.")
        return
    
    # Token length constraint
    original_tokens = len(st.session_state['current_ori_statement'].split())
    input_tokens = len(input_txt.split())
    if abs(input_tokens - original_tokens) > 20:  # Check if the input is within 20 tokens of the original
        st.warning(f"Your rewritten statement must be within 20 words of the original statement's length (i.e., {original_tokens} +/- 20 words). Your input has {input_tokens} words.")
        return
    
    st.session_state['current_repharsed_text'] = str(input_txt)
    st.session_state['goto_step_page'] = 1
    st.session_state.main_task_3_submit_count += 1
    
if 'goto_step_page' in st.session_state and st.session_state['goto_step_page'] == 1:
    st.session_state['goto_step_page'] = 0
    st.switch_page("pages/experiment_step_3_page.py")

# Initialize submission count in session state
if 'main_task_3_submit_count' not in st.session_state:
    st.session_state.main_task_3_submit_count = 0

# Page data
paraphrase_classification = "X"
classification_score = -1

# Load statements and select a random one
if 'new_statement' not in st.session_state or st.session_state['new_statement'] == 1:
    statement = load_statements()
    st.session_state['store_data'] = 0
    #random_statement = statements.sample(n=1).iloc[0]
    statement_text = statement['text_truncated']
    condition = statement['condition']

    #states
    st.session_state['statement_id'] = statement['index']
    st.session_state['current_ori_statement'] = statement_text
    st.session_state['current_ori_statement_condition'] = condition
    st.session_state['paraharse_start_time'] = datetime.datetime.now()

# Initial classification
paraphrase_classification, classification_score = chatloop(frase=str(st.session_state['current_ori_statement']))

# Page description
text_container_1 = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
text_container_4 = st.empty()
input_container = st.empty()
submit_container = st.empty()
input_txt = input_container.text_area("Write your text below:", height=250, placeholder=st.session_state['current_ori_statement'])
nav_col1, nav_col2 = st.columns(2,gap="medium")
st.button("Submit",on_click=goto_exp_step)

# Display instruction
load_instruction(text_container_1, feedback_container, progr_cont, text_container_2, text_container_3, text_container_4, input_container,submit_container,
                paraphrase_classification = paraphrase_classification,
                classification_score = classification_score)
