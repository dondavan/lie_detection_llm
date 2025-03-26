import streamlit as st

st.title("Feedback")
st.write("Please provide us with feedback about the study. Your feedback is valuable to us and will help us improve our study.")

st.write("**1. How much were you motivated to perform well?**")
st.session_state.motivation_scale = st.slider("0 = Not at all, 10 = Very much", min_value=0, max_value=10, value=5, step=1)

st.write("**2. How difficult did you find the study?**")
st.session_state.difficulty_scale = st.slider("0 = Very easy, 10 = Very difficult", min_value=0, max_value=10, value=5, step=1)

st.write("What strategies did you use to complete the task and flip the classification label?")
st.session_state.strategies = st.text_area("Strategies")

st.write("Optionally, you can leave any remarks or feedback you have about this experiment. Please click on the button below to submit your feedback.")
st.session_state.feedback = st.text_area("Feedback")

if st.button("Submit Feedback"):
    update_progress()
    feedback_data = [
        st.session_state.like_scale,
        st.session_state.difficulty_scale,
        st.session_state.feedback]
    
    # Retrieve response_data and questions_data from session state
    questions_data = st.session_state.questions_data
    
    # Concatenate all data into a single list
    combined_data =  questions_data + feedback_data 
    # submit_to_sheet_2(combined_data)
    st.write("Thank you for your feedback.")
    st.switch_page("pages/end_page.py")