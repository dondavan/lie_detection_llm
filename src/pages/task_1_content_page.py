import streamlit as st
from utility import chatloop, insert_to_sql
import datetime

st.title("Training Phase 1: Write a Lie or a Truth")
st.write("**Please write a deceptive or a truthful statement.**")

st.write("A lie is a statement of false information intended to deceive or mislead the receiver.")
st.write("A truth is a statement that presents information that is believed to be correct with no intention to mislead the receiver.")
st.write("**Note:** You can submit up to 5 statements before proceeding. When you click 'Submit', you will receive feedback from the AI model and see the real predictions of the model for your statement.")
st.write("**IMPORTANT:** If the page does not respond, press submit again. DO NOT REFRESH THE PAGE.")


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
if submit_cont.button("Submit",key="submit"):
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
            st.warning("Please write a deceptive or truthful statement before submitting.")
    else:
        st.error("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")
        
# Add a "Next" button to proceed to the next page
if st.button("Next"):
    st.switch_page("pages/task_2_content_page.py")