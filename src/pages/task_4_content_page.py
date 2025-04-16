import streamlit as st
import pandas as pd
from utility import chatloop, load_statements
import time

st.title("Task 4: Switch the Credibility with Contraints")

def load_instruction(text_container_1,text_container_2,text_container_3,input_container,submit_container,paraphrase_classfication = "X",classfication_score = -1):
    # Display the statement and instructions
    if st.session_state['current_ori_statement_condition'] == "truthful":
        condition_1 = "truthful"
        condition_2 = "deceptive"
    else:
        condition_1 = "deceptive"
        condition_2 = "truthful"

    text_container_1.markdown(f"This is a {condition_1} statement. Rewrite this statement so that it appears {condition_2} to an automated deception classifier. **Please maintain the original meaning of the statement, ensure grammaticality, and that your rewrite appears natural.**")
    text_container_2.markdown(f"Original statement: {st.session_state['current_ori_statement']}")

    if paraphrase_classfication == "T":
        text_container_3.markdown("The paragraph is true. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(classfication_score))
    elif paraphrase_classfication == "F":
        text_container_3.markdown("The paragraph is false. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(classfication_score))
    
    st.session_state['new_statement'] = 0

def goto_exp_step():
    st.session_state['current_repharsed_text'] = str(input_txt)
    st.session_state['goto_step_page'] = 1

if 'goto_step_page' in st.session_state and st.session_state['goto_step_page'] == 1:
    st.session_state['goto_step_page'] = 0
    st.switch_page("pages/feedback_task_4_page.py")

# Page description
text_container_1 = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
input_container = st.empty()
submit_container = st.empty()
input_txt = input_container.text_area("Write your text below:")
nav_col1, nav_col2 = st.columns(2,gap="medium")
st.button("SUBMIT",on_click=goto_exp_step)

# Page data
paraphrase_classfication = "X"
classfication_score = -1

# Load statements and select a random one
if 'new_statement' not in st.session_state or st.session_state['new_statement'] == 1:
    statements = load_statements()
    random_statement = statements.sample(n=1).iloc[0]
    statement_text = random_statement['text']
    condition = random_statement['condition']

    #states
    st.session_state['current_ori_statement'] = statement_text
    st.session_state['current_ori_statement_condition'] = condition

# Initial classification
paraphrase_classfication, classfication_score = chatloop(frase=str(st.session_state['current_ori_statement']))
# Display instruction
load_instruction(text_container_1,text_container_2,text_container_3,input_container,submit_container,
                paraphrase_classfication = paraphrase_classfication,
                classfication_score = classfication_score)