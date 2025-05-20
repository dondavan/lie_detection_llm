import streamlit as st
from utility import chatloop, insert_to_sql
import datetime

st.title("Training Task 1: Write a Lie or a Truth")
st.write("**Please write a lie or a truth.**")

st.write("A lie is a statement of false information intended to deceive or mislead the receiver.")
st.write("A truth is a statement that presents information that is believed to be correct with no intention to mislead the receiver.")
st.write("**Note:** This is an exploratory page. You can submit multiple statements (maximum 5) before clicking next. To resubmit, first delete your previous statement, then click 'Submit' again. This allows you to explore how the AI classifies lies.")


st.session_state['paraharse_start_time'] = datetime.datetime.now()

# Initialize submission count in session state
if 'task_1_submit_count' not in st.session_state:
    st.session_state.task_1_submit_count = 0

# Create containers for dynamic updates
input_container = st.empty()
submit_cont = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()

# Input for the user to write their statement
user_input = input_container.text_area("Write your statement here:")

# Submit button to process the input
if submit_cont.button("Submit"):
    if st.session_state.task_1_submit_count < 5:  # Check if the limit is reached
        if user_input.strip():  # Ensure the input is not empty
            st.session_state['current_repharsed_text'] = user_input

            st.session_state['paraharse_end_time'] = datetime.datetime.now()

            start_time = st.session_state['paraharse_start_time'].strftime('%Y-%m-%d %H:%M:%S')
            end_time = st.session_state['paraharse_end_time'].strftime('%Y-%m-%d %H:%M:%S')

            pid = st.session_state['pid']
            
            # Generate feedback using the model
            risposta, prob = chatloop(user_input)
            # Insert into cloud sql
            parameters = {  "pid": pid,
                            "os_id": 'task1_dummy',
                            "os": 'task1_dummy',
                            "os_c": -1,
                            "os_cp": -1,
                            "paras":st.session_state['current_repharsed_text'],
                            "paras_c": risposta,
                            "paras_cp": prob,
                            "start_time":start_time,
                            "end_time":end_time}
            
            insert_to_sql(parameters)

            feedback_container.markdown(
                f"### Model Feedback\n"
                f"The model predicts that your statement is classified as **{'TRUTHFUL' if risposta == 1 else 'DECEPTIVE'}**.\n"
                f"**Confidence Score:** {prob:.2f}%"
            )
            progr_cont.progress(int(prob))  # Display progress bar for confidence score

            # Increment the submission count
            st.session_state.task_1_submit_count += 1
            st.info(f"Submission {st.session_state.task_1_submit_count}/5")
            
        else:
            st.warning("Please write a lie before submitting.")
    else:
        st.error("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")
        
# Add a "Next" button to proceed to the next page
if st.button("Next"):
    st.switch_page("pages/task_2_content_page.py")