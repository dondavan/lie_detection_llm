import streamlit as st

st.title("Instructions")
st.write(":book: In this experiment, you will read **3** short statements about past experiences. Each statement is either truthful :white_check_mark: or deceptive :lying_face:.")
st.write("Your task is to paraphrase these statements. Specifically, your rewrite is meant to make the statement appear opposite in credibility compared to how they were originally classified by an automated deception classifier.")
st.write("Further, your rewrite has to maintain the original meaning, be grammatically correct, and appear natural. Naturalness is described by fluency, readability, and coherence.")

st.write("""To help you with your task, we provide you with the predictions of a state-of-the-art lie detection algorithm based on artificial intelligence (AI) :robot_face:""")
st.write("This feedback shows you whether the AI thinks the statement is a lie or a truth and how confident it is in its classification. Your goal is to change the AI's confidence score (lower the percentage shown for the initial statement) through your rewrites.")
st.write("In total you will have 10 attempts to change the confidence score as much as possible. If you manage to change the class the AI thinks the statement belongs to (truth or lie), you will move on to the next statement.")
st.write("You'll undergo a guided training procedure to make you familiar with the task on the next few pages.")

st.write("**Please note that you should read and rewrite the statements carefully.**")

if st.button("Next"):
    st.switch_page("pages/specific_instructions_page.py")