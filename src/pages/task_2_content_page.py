import streamlit as st

st.title("Task 2: Write a Truth")
st.write("**Please write a truth.**")

# Create containers for dynamic updates
input_container = st.empty()
submit_cont = st.empty()
feedback_container = st.empty()
progr_cont = st.empty()

# Input for the user to write their statement
user_input = input_container.text_area("Write your statement here:")

# Submit button to process the input
if submit_cont.button("Submit Task 2"):
    if user_input.strip():  # Ensure the input is not empty
        st.session_state.task_2_input = user_input
        update_progress()

        # Generate feedback using the model
        #risposta, prob = chatloop(user_input)
        feedback_container.markdown(
            f"### Model Feedback\n"
            f"The model predicts that your statement is classified as **{'Truthful' if risposta == 'T' else 'Deceptive'}**.\n"
            f"**Confidence Score:** {prob:.2f}%"
        )
        progr_cont.progress(int(prob))  # Display progress bar for confidence score
    else:
        st.warning("Please write a truth before submitting.")

# Add a "Next" button to proceed to the next page
if st.button("Next"):
    st.switch_page("pages/experiment_intro_page.py")
    #st.experimental_rerun()