import streamlit as st
from utility import chatloop

st.title("Task 2: Write a Truth")
st.write("**Please write a truth.**")

st.write("A truth is a statement that presents information that is believed to be correct with no intent to mislead.")
st.write("**Note:** This is an exploratory page. You can submit multiple statements (maximum 5) before clicking next. To resubmit, first delete your previous statement, then click 'Submit' again. This allows you to explore how the AI classifies truths.")

# Initialize submission count in session state
if 'task_2_submit_count' not in st.session_state:
    st.session_state.task_2_submit_count = 0

# Create containers for dynamic updates
input_container = st.empty()
submit_cont = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()

# Input for the user to write their statement
user_input = input_container.text_area("Write your statement here:")

# Submit button to process the input
if submit_cont.button("Submit Task 2"):
    if st.session_state.task_2_submit_count < 5:  # Check if the limit is reached
        if user_input.strip():  # Ensure the input is not empty
            st.session_state.task_2_input = user_input

            # Generate feedback using the model
            risposta, prob = chatloop(user_input)
            feedback_container.markdown(
                f"### Model Feedback\n"
                f"The model predicts that your statement is classified as **{'Truthful' if risposta == 'T' else 'Deceptive'}**.\n"
                f"**Confidence Score:** {prob:.2f}%"
            )
            progr_cont.progress(int(prob))  # Display progress bar for confidence score

            # Increment the submission count
            st.session_state.task_2_submit_count += 1
            st.info(f"Submission {st.session_state.task_2_submit_count}/5")
        else:
            st.warning("Please write a truth before submitting.")
    else:
        st.error("You have reached the maximum number of submissions (5). Please click 'Next' to proceed.")
        
# Add a "Next" button to proceed to the next page
if st.button("Next"):
    st.switch_page("pages/task_3_content_page.py")
    #st.experimental_rerun()