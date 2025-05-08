import streamlit as st
import uuid

st.title("Instructions")
st.write(":book: In this experiment, you will read **3** short statements about past experiences. Each statement is either truthful :white_check_mark: or deceptive :lying_face:. The statements have been shortened and might at times end aprubtly.")
st.write("Apart from the statements, we provide you with the predictions of a state-of-the-art lie detection algorithm based on artificial intelligence (AI) :robot_face:.")
st.write("This shows you whether the AI thinks the statement is a deceptive or a truthful and how confident it is in its classification (Confidence Score).")

st.write("Your task is to **paraphrase** these statements. Specifically, your rewrite is meant to make the statement appear opposite in credibility compared to how they were originally classified by the AI (deceptive or truthful).")
st.write("In total you will have **10** attempts per statement to decrease the **confidence score** of the AI's original prediction as much as possible. If you manage to change the original prediction (truthful or deceptive), you will immediately move on to the next statement.")
st.write("Importantly, your rewrite has to maintain the meaning of the original statement, be grammatically correct, and appear natural. A natural rewrite describes a fluent, readable, and coherent text.")
st.write("**Please read and rewrite the statements carefully.**")

st.session_state['pid'] = str(uuid.uuid4())
st.session_state['store_data'] = 0

if st.button("Next"):
    st.switch_page("pages/stepwise_training_page.py")