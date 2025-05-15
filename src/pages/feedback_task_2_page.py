import streamlit as st
import pandas as pd
from utility import chatloop, load_statements, insert_to_sql
import datetime

st.title("Training Task 2: Fool the AI")

def feedback_page(text_container_1, feedback_container_1, progr_cont_1, text_container_2, feedback_container_2, progr_cont_2, input_container, submit_container, nav_col_1, nav_col_2,
                  current_ori_statement, current_repharsed_text):
    # Classification for the original statement
    ori_classification, ori_score = chatloop(frase=current_ori_statement)

    # Initial classification
    paraphrase_classfication, classfication_score = chatloop(frase=current_repharsed_text)




    st.session_state['ori_classification'] = ori_classification
    st.session_state['ori_score'] = ori_score

    st.session_state['paraphrase_classfication'] = paraphrase_classfication
    st.session_state['classfication_score'] = classfication_score

    st.session_state['paraharse_end_time'] = datetime.datetime.now()

    start_time = st.session_state['paraharse_start_time'].strftime('%Y-%m-%d %H:%M:%S')
    end_time = st.session_state['paraharse_end_time'].strftime('%Y-%m-%d %H:%M:%S')

    # Insert into cloud sql
    parameters = {  "pid": st.session_state['pid'],
                    "os_id": st.session_state['statement_id'],
                    "os": st.session_state['current_ori_statement'],
                    "os_c":st.session_state['ori_classification'],
                    "os_cp":st.session_state['ori_score'],
                    "paras":st.session_state['current_repharsed_text'],
                    "paras_c":st.session_state['paraphrase_classfication'],
                    "paras_cp":st.session_state['classfication_score'],
                    "start_time":start_time,
                    "end_time":end_time}
    
    # Only store once for each statement
    if(st.session_state['store_data'] == 0):
        insert_to_sql(parameters)
        st.session_state['store_data'] = 1
    
    
    text_container_1.markdown(f"**Original statement:** {current_ori_statement}")

    feedback_container_1.markdown(
        f"The AI classifies this statement as **{'TRUTHFUL' if ori_classification == 1 else 'DECEPTIVE'}**.\n"
        f"Confidence Score: **{ori_score:.2f}%**"
    )
    progr_cont_1.progress(int(ori_score)) 

    text_container_2.markdown(f"**Your statement:** {current_repharsed_text}")

    feedback_container_2.markdown(
        f"The AI classifies this statement as **{'TRUTHFUL' if paraphrase_classfication == 1 else 'DECEPTIVE'}**.\n"
        f"Confidence Score: **{classfication_score:.2f}%**"
    )
    progr_cont_2.progress(int(classfication_score)) 

def click_submit():
    if not input_txt.strip():  # Check if the input is empty
        st.warning("Please write a statement before submitting.")
        return
    
    if st.session_state.task_3_submit_count < 5:  # Check if the limit is reached
        st.session_state['current_repharsed_text'] = str(input_txt)
        st.session_state['submit_view'] = 0
        st.session_state.task_3_submit_count += 1
        st.session_state['store_data'] = 0
    else:
        st.error("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")

def click_retry():
    if st.session_state.task_3_submit_count >= 5:  # Check if the limit is reached
        st.warning("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")
    else:
        st.session_state['paraharse_start_time'] = datetime.datetime.now()
        st.session_state['submit_view'] = 1

def click_next():
    st.session_state['new_statement'] = 1
    st.session_state['goto_new_statement'] = 1

# Page description
text_container_1 = st.empty()
feedback_container_1 = st.empty()
progr_cont_1 = st.empty()
text_container_2 = st.empty()
feedback_container_2 = st.empty()
progr_cont_2 = st.empty()
input_container = st.empty()
submit_container = st.empty()
nav_col1, nav_col2 = st.columns(2, gap="medium")

# states
current_ori_statement = st.session_state['current_ori_statement']
current_repharsed_text = st.session_state['current_repharsed_text']

# Display feedback
feedback_page(text_container_1, feedback_container_1, progr_cont_1, text_container_2, feedback_container_2, progr_cont_2, input_container, submit_container, nav_col1, nav_col2,
              current_ori_statement=current_ori_statement, 
              current_repharsed_text=current_repharsed_text)

# Navigation logic
if 'goto_new_statement' in st.session_state and st.session_state['goto_new_statement'] == 1:
    st.session_state['goto_new_statement'] = 0
    st.switch_page("pages/task_3_content_page.py")

if 'submit_view' in st.session_state and st.session_state['submit_view'] == 1:
    nav_col1 = st.empty()
    nav_col2 = st.empty()
    input_txt = input_container.text_area("Write your text below:", height=250, placeholder=current_repharsed_text)
    submit_butt = submit_container.button('Submit',on_click = click_submit)

if 'submit_view' not in st.session_state or st.session_state['submit_view'] == 0:
    retry_butt = nav_col1.button("Retry",on_click=click_retry)
    next_butt = nav_col2.button("Next",on_click=click_next)

# Display submission count
st.info(f"Submissions used: {st.session_state.task_3_submit_count}/5")