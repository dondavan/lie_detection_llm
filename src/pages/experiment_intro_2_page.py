import streamlit as st
import pandas as pd
from utility import chatloop, load_statements
import time

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
        f"The AI classifies this statement as **{'Truthful' if paraphrase_classification == 'T' else 'Deceptive'}**.\n"
        f"Credibility Score: **{classification_score:.2f}%**"
    )
    progr_cont.progress(int(classification_score))  # Display progress bar for credibility score

    text_container_2.markdown(
        f"Rewrite this statement so that it appears **{condition_2}** to the AI.\n"
        "Please maintain the statements **original meaning**, ensure that it is **grammatically correct**, and appears **natural**. A **natural** statement is coherent, fluent and readable.\n"
        "You have 10 attempts to rewrite. If you manage to flip the class (truthful to deceptive or deceptive to truthful) before that, please proceed to the next page.")
    original_tokens = len(st.session_state['current_ori_statement'].split())
    text_container_3.markdown(f"Your rewritten statement must be within 20 words of the original statement's length **({original_tokens} words)**.")
    text_container_4.markdown(f"**WARNING:** Due to delay with the AI model, you might have to click the submit button a second time after a brief period.")

    st.session_state['new_statement'] = 0

def goto_exp_step():
    if not input_txt.strip():  # Check if the input is empty
        st.warning("Please write a statement before submitting.")
        return
    
    # Token length constraint
    original_tokens = len(st.session_state['current_ori_statement'].split())
    input_tokens = len(input_txt.split())
    if abs(input_tokens - original_tokens) > 20:  # Check if the input is within 20 tokens of the original
        st.warning(f"Your rewritten statement must be within 20 words of the original statement's length ({original_tokens} words). Your input has {input_tokens} words.")
        return
    
    st.session_state['current_repharsed_text'] = str(input_txt)
    st.session_state['goto_step_page'] = 1
    st.session_state.main_task_2_submit_count += 1
    
if 'goto_step_page' in st.session_state and st.session_state['goto_step_page'] == 1:
    st.session_state['goto_step_page'] = 0
    st.switch_page("pages/experiment_step_2_page.py")

# Initialize submission count in session state
if 'main_task_2_submit_count' not in st.session_state:
    st.session_state.main_task_2_submit_count = 0

# Page description
text_container_1 = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
text_container_4 = st.empty()
input_container = st.empty()
submit_container = st.empty()
input_txt = input_container.text_area("Write your text below:")
nav_col1, nav_col2 = st.columns(2,gap="medium")
st.button("Submit",on_click=goto_exp_step)

# Page data
paraphrase_classification = "X"
classification_score = -1

# Load statements and select a random one
if 'new_statement' not in st.session_state or st.session_state['new_statement'] == 1:
    statements = load_statements()
    random_statement = statements.sample(n=1).iloc[0]
    statement_text = random_statement['text_truncated']
    condition = random_statement['condition']

    #states
    st.session_state['current_ori_statement'] = statement_text
    st.session_state['current_ori_statement_condition'] = condition

# Initial classification
paraphrase_classification, classification_score = chatloop(frase=str(st.session_state['current_ori_statement']))
# Display instruction
load_instruction(text_container_1, feedback_container, progr_cont, text_container_2, text_container_3, text_container_4, input_container,submit_container,
                paraphrase_classification = paraphrase_classification,
                classification_score = classification_score)
