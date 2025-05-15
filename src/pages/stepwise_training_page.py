import streamlit as st

st.title("Training Procedure")
st.write("You will now perform three training tasks to familiarize yourself with the task.")

st.write("**NOTE**: The following pages involve AI feedback which might cause some delay when changing pages.")
st.write("**IMPORTANT**: Please do not use any outside tools (e.g., Google, ChatGPT) to assist you in this task. This is a test of your own ability to fool the AI.")

if st.button("Next"):
    st.switch_page("pages/task_1_content_page.py")