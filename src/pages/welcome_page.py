import streamlit as st

st.title("Welcome to the _'ADVERSARIAL PARAPHRASING ATTACKS ON AUTOMATED DECEPTION CLASSIFIERS'_ study")
st.write("""This study explores how robust automated deception classifiers are to modifications - paraphrases - to a statement they classify. 
             After you have consented to participate in this experiment, we will give you detailed instructions. **Please read them carefully.**
             \nOnce you complete the experiment, you will be redirected to Prolific.""")
    
if st.button("Next"):
    st.switch_page("pages/consent_page.py")