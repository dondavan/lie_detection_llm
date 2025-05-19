import streamlit as st

st.title("Instructions")
st.write(":book: In this experiment, you will read **3** short statements written by participants in another study. A statement is either truthful :white_check_mark: or deceptive :lying_face:. Some statements have been truncated.")
st.write("Alongside each statement, you see the predictions of a state-of-the-art AI lie detection algorithm that was trained on a large dataset of truths and lies :robot_face:.")
st.write("The predictions show you whether the AI classifies the statement as deceptive or truthful and how confident it is about this classification. This is shown as the Confidence Score. The closer the confidence score is to 100%, the higher the confidence of the model’s prediction. Confidence values closer to 50% indicate uncertainty with 50% implying equal confidence in this statement being deceptive and truthful")

st.write("Your task is to **rewrite** these statements with a specific task in mind. Specifically, your task is to rewrite or paraphrase the statements so that they are classified as the opposite by the model. For example, when the original prediction is that a statement is truthful, you need to modify it so that it is classified as deceptive. Vice versa, when a statement is initially classified as deceptive by the model, your task is to modify it to be classified as truthful. You will be able to see how your modifications affected the model by directly interacting with it and receive live predictions for your modified statement.")
st.write("In total you will have **10** attempts per statement to decrease the **confidence score** of the AI's original prediction as much as possible. If you manage to change the original prediction (truthful or deceptive), you will immediately move on to the next statement.")
st.write("There is one very important condition to be met: You must maintain the meaning of the original statement, be grammatically correct, and appear natural.")
st.write("**Please read and rewrite the statements carefully.**")
st.write("**IMPORTANT**: Please do not refresh the page or click the back button during the study, as it may cause errors in the system.")


if st.button("Next"):
    st.switch_page("pages/stepwise_training_page.py")