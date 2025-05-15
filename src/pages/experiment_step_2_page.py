import streamlit as st
import pandas as pd
from utility import chatloop, load_statements, insert_to_sql
import datetime

st.title("Main Task")
 
def feedback_page(text_container_1, feedback_container_1, progr_cont_1, text_container_2, feedback_container_2, progr_cont_2, text_container_3, input_container, submit_container, nav_col_1, nav_col_2,
                  current_ori_statement, current_repharsed_text):
    if st.session_state['current_ori_statement_condition'] == "truthful":
        condition_1 = "truthful"
        condition_2 = "deceptive"
    else:
        condition_1 = "deceptive"
        condition_2 = "truthful"

    # Classification for the original statement
    ori_classification, ori_score = chatloop(frase=current_ori_statement)
    # Initial classification
    paraphrase_classification, classification_score = chatloop(frase=current_repharsed_text)


    st.session_state['ori_classification'] = ori_classification
    st.session_state['ori_score'] = ori_score

    st.session_state['paraphrase_classfication'] = paraphrase_classification
    st.session_state['classfication_score'] = classification_score

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
        f"The AI classifies this statement as **{'TRUTHFUL' if paraphrase_classification == 1 else 'DECEPTIVE'}**.\n"
        f"Confidence Score: **{classification_score:.2f}%**"
    )
    progr_cont_2.progress(int(classification_score))
    opposite_classification = 'DECEPTIVE' if ori_classification == 1 else 'TRUTHFUL'
    # Conditionally display text_container_3 after "Retry" is clicked
    if 'submit_view' in st.session_state and st.session_state['submit_view'] == 1:
        text_container_3.markdown(
            f"Rewrite this statement so that it appears **{opposite_classification}** to the AI.\n"
            "Please maintain the statement's **original meaning**, ensure that it is **grammatically correct**, and appears **natural**. A **natural** statement is coherent, fluent, and readable."
        )
    # Return classifications to determine button visibility
    return ori_classification, paraphrase_classification 

def click_submit():
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
    st.session_state['submit_view'] = 0
    st.session_state.main_task_2_submit_count += 1
    st.session_state['store_data'] = 0
    

def click_retry():
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
text_container_3 = st.empty()
input_container = st.empty()
submit_container = st.empty()
nav_col1, nav_col2 = st.columns(2, gap="medium")

# States
current_ori_statement = st.session_state['current_ori_statement']
current_repharsed_text = st.session_state['current_repharsed_text']

# Display feedback
ori_classification, paraphrase_classification = feedback_page(
    text_container_1, feedback_container_1, progr_cont_1, 
    text_container_2, feedback_container_2, progr_cont_2, text_container_3,
    input_container, submit_container, nav_col1, nav_col2,
    current_ori_statement=current_ori_statement, 
    current_repharsed_text=current_repharsed_text)

if 'goto_new_statement' in st.session_state and st.session_state['goto_new_statement'] == 1:
    st.session_state['goto_new_statement'] = 0
    st.switch_page("pages/experiment_intro_3_page.py")

if ori_classification != paraphrase_classification:
    # Show success message and "Next" button only
    st.success("You have successfully flipped the class the AI thought the statement belonged to. Please proceed to the next statement.")
    next_butt = nav_col2.button("Next", on_click=click_next)
elif st.session_state.main_task_2_submit_count >= 10:
    st.warning("You have reached the maximum number of rewrites (10) for this statement. Please proceed to the next statement.")
    next_butt = nav_col2.button("Next", on_click=click_next)
else:
    # Show "Retry" and "Submit" buttons if classifications are the same
    if 'submit_view' in st.session_state and st.session_state['submit_view'] == 1:
        nav_col1 = st.empty()
        nav_col2 = st.empty()
        input_txt = input_container.text_area("Write your text below:", height=250, placeholder=current_repharsed_text)
        submit_butt = submit_container.button('Submit', on_click=click_submit)

    if 'submit_view' not in st.session_state or st.session_state['submit_view'] == 0:
        retry_butt = nav_col1.button("Retry", on_click=click_retry)

# Display submission count
st.info(f"Submissions used: {st.session_state.main_task_2_submit_count}/10")