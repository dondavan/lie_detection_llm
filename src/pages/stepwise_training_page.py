import streamlit as st

st.title("Training Procedure")
st.write("You will start with a training phase to familiarize yourself with the task. The training phases will guide you through the task requirements step-by-step.")

st.write("**NOTE**: The following pages involve live AI feedback which might cause some delay when loading new pages.")
st.write("**IMPORTANT**: Please do not use any outside tools (e.g., Google, ChatGPT) to assist you in this task. This study is a test of your own ability.")

if st.button("Next"):
    st.switch_page("pages/task_1_content_page.py")