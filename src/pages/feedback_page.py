import streamlit as st

st.title("Feedback")
st.write("Please provide us with feedback about the study. Your feedback is valuable to us and will help us improve our study.")

# Initialize session state variables if not already set
if 'motivation_scale' not in st.session_state:
    st.session_state.motivation_scale = 5
if 'difficulty_scale' not in st.session_state:
    st.session_state.difficulty_scale = 5
if 'strategies' not in st.session_state:
    st.session_state.strategies = ""
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'questions_data' not in st.session_state:
    st.session_state.questions_data = []

# Question 1: Motivation
st.write("**1. How motivated were you to perform well?**")
st.session_state.motivation_scale = st.slider("0 = Not at all, 10 = Very much", min_value=0, max_value=10, value=st.session_state.motivation_scale, step=1)

# Question 2: Difficulty
st.write("**2. How difficult did you find the study?**")
st.session_state.difficulty_scale = st.slider("0 = Very easy, 10 = Very difficult", min_value=0, max_value=10, value=st.session_state.difficulty_scale, step=1)

# Question 3: Strategies
st.write("What strategies did you use to complete the task and flip the classification label?")
st.session_state.strategies = st.text_area("Strategies", value=st.session_state.strategies)

# Optional Feedback
st.write("Optionally, you can leave any remarks or feedback you have about this experiment. Please click on the button below to submit your feedback.")
st.session_state.feedback = st.text_area("Feedback", value=st.session_state.feedback)

# Submit Feedback Button
if st.button("Submit Feedback"):
    # Validation: Ensure all required fields are answered
    if not st.session_state.strategies.strip():
        st.warning("Please answer all questions before submitting.")
    elif st.session_state.motivation_scale is None:
        st.warning("Please answer all questions before submitting.")
    elif st.session_state.difficulty_scale is None:
        st.warning("Please answer all questions before submitting.")
    else:
        # Collect feedback data
        feedback_data = [
            st.session_state.motivation_scale,
            st.session_state.difficulty_scale,
            st.session_state.strategies,
            st.session_state.feedback
        ]
        
        # Retrieve response_data and questions_data from session state
        questions_data = st.session_state.questions_data
        
        # Concatenate all data into a single list
        combined_data = questions_data + feedback_data
        
        # Submit the data (placeholder for actual submission logic)
        # submit_to_sheet_2(combined_data)
        
        st.write("Thank you for your feedback.")
        st.switch_page("pages/end_page.py")