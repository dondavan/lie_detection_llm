import streamlit as st

st.title("Welcome to the _'REWRITING TRUTHS AND LIES'_ study")
st.write("""This study explores how robust automated deception classifiers are to changes (paraphrases) in the statements they classify.  
             \nWe will give you detailed instructions once you have consented to participate in this experiment. **Please read them carefully.**
             \nOnce you complete the experiment, you will be redirected to Prolific.""")
    
if st.button("Next"):
    st.switch_page("pages/consent_page.py")