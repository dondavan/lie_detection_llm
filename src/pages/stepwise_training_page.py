import streamlit as st

st.title("Training Procedure")
st.write("You will now perform four subtasks to familiarize yourself with the task.")

st.write("**WARNING**: The training procedure and the main task involve AI feedback which might cause some delay when changing pages.")

if st.button("Next"):
    st.switch_page("pages/task_1_content_page.py")