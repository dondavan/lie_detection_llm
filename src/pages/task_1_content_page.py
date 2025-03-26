import streamlit as st
from utility import chatloop

st.title("Task 1: Write a Lie")
st.write("**Please write a lie.**")

# Create containers for dynamic updates
input_container = st.empty()
submit_cont = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()

# Input for the user to write their statement
user_input = input_container.text_area("Write your statement here:")

# Submit button to process the input
if submit_cont.button("Submit Task 1"):
    if user_input.strip():  # Ensure the input is not empty
        st.session_state.task_1_input = user_input

        # Generate feedback using the model
        risposta, prob = chatloop(user_input)
        feedback_container.markdown(
            f"### Model Feedback\n"
            f"The model predicts that your statement is classified as **{'Truthful' if risposta == 'T' else 'Deceptive'}**.\n"
            f"**Confidence Score:** {prob:.2f}%"
        )
        progr_cont.progress(int(prob))  # Display progress bar for confidence score

    else:
        st.warning("Please write a lie before submitting.")

# Add a "Next" button to proceed to the next page
if st.button("Next"):
    st.switch_page("pages/task_2_content_page.py")