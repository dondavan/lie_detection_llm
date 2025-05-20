import streamlit as st
import uuid

prolific_id = st.query_params.get_all("PROLIFIC_PID")

if len(prolific_id) == 0 :
    st.session_state['pid'] = str(uuid.uuid4())
else:
    st.session_state['pid'] = prolific_id[0]

st.title("Welcome to the _'REWRITING TRUTHS AND LIES'_ study")
st.write("""In this study, your task is to interact with an AI model that classifies statements as truthful or deceptive.  
             \nOn the next pages you will receive detailed task instructions. 
             \nOnce you complete the experiment, you will be redirected to Prolific.""")
    
if st.button("Next"):
    st.switch_page("pages/consent_page.py")