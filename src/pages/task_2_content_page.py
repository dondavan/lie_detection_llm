import streamlit as st
import pandas as pd
from utility import chatloop, load_statements, load_statements_2, insert_to_sql
import datetime

st.title("Training Phase 2: Fool the AI")

def load_instruction(text_container_1, feedback_container, progr_cont, text_container_2, text_container_3, input_container, submit_container, paraphrase_classfication="X", classfication_score=-1):
    # Display the statement and instructions
    if st.session_state['current_ori_statement_condition'] == "truthful":
        condition_1 = "truthful"
        condition_2 = "deceptive"
    else:
        condition_1 = "deceptive"
        condition_2 = "truthful"

    text_container_1.markdown(f"**Original statement:** {st.session_state['current_ori_statement']}")
   
    feedback_container.markdown(
        f"The AI classifies this statement as **{'TRUTHFUL' if paraphrase_classfication == 1 else 'DECEPTIVE'}**.\n"
        f"Confidence Score: **{classfication_score:.2f}%**"
    )
    progr_cont.progress(int(classfication_score))  # Display progress bar for credibility score

    text_container_2.markdown(f"Rewrite this statement so that it appears **TRUTHFUL** to the AI. You can submit up to 5 attempts.")
    text_container_3.markdown(f"**IMPORTANT:** Due to delay with live feedback from the AI model, you have to click the submit button a second time after a brief period.")

    st.session_state['new_statement'] = 0

def goto_exp_step():
    if not input_txt.strip():  # Check if the input is empty
        st.warning("Please write a statement before submitting.")
        return
    if st.session_state.task_3_submit_count < 5:  # Check if the limit is reached
        st.session_state['current_repharsed_text'] = str(input_txt)
        st.session_state['goto_step_page'] = 1
        st.session_state.task_3_submit_count += 1
    else:
        st.error("You have reached the maximum number of rewrites for this statement (5). Please proceed to the next page.")

if 'goto_step_page' in st.session_state and st.session_state['goto_step_page'] == 1:
    st.session_state['goto_step_page'] = 0
    st.switch_page("pages/feedback_task_2_page.py")

# Initialize submission count in session state
if 'task_3_submit_count' not in st.session_state:
    st.session_state.task_3_submit_count = 0

# Page data
paraphrase_classfication = "X"
classfication_score = -1

# Load statements and select a fixed "deceptive" statement
if 'new_statement' not in st.session_state or st.session_state['new_statement'] == 1:
    statements = load_statements_2()  
    st.session_state['store_data'] = 0
    deceptive_statements = statements[statements['condition'] == 'deceptive']  
    random_statement = deceptive_statements.iloc[0]  # Select the first statement to ensure consistency
    statement_text = random_statement['text_truncated']
    condition = random_statement['condition']

    # Save states
    st.session_state['statement_id'] = random_statement['index']
    st.session_state['current_ori_statement'] = statement_text
    st.session_state['current_ori_statement_condition'] = condition

# Initial classification
ori_classfication, classfication_score = chatloop(frase=str(st.session_state['current_ori_statement']))

# Page description
text_container_1 = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()
text_container_2 = st.empty()
text_container_3 = st.empty()
input_container = st.empty()
submit_container = st.empty()
input_txt = input_container.text_area("Write your text below:", height=250, placeholder=st.session_state['current_ori_statement'])
nav_col1, nav_col2 = st.columns(2,gap="medium")
st.button("Submit Task",on_click=goto_exp_step, key="submit")



st.markdown("""
    <script>
    const submitBtn = window.parent.document.querySelector('button[key="submit"]');
    if (submitBtn) {
        submitBtn.addEventListener('mousedown', function() {
            const textareas = window.parent.document.querySelectorAll('textarea');
            textareas.forEach(t => t.blur());
        });
    }
    </script>
    """, unsafe_allow_html=True)


# Display instruction
load_instruction(text_container_1, feedback_container, progr_cont, text_container_2, text_container_3, input_container,submit_container,
                paraphrase_classfication = ori_classfication,
                classfication_score = classfication_score)