import streamlit as st

st.title("Training Procedure")
st.write("You will now perform four subtasks as part of a stepwise training procedure to familiarize yourself with the task.")

if st.button("Next"):
    st.switch_page("pages/task_1_content_page.py")