import streamlit as st

st.title("Main Task")
st.write("You are about to start the main task. Here are some pointers of what to keep in mind:")

st.markdown(
    """
    - **Understand the Task**: Your goal is to paraphrase statements to lower the AI's confidence score or change the class (truthful or deceptive) it predicts the statement to belong to.
    - **Maintain Meaning**: Ensure your paraphrases preserve the original meaning of the statement.
    - **Use of Language**: Use natural and grammatically correct language to rewrite the statements.
    - **Tips**: Avoid simply reordering words; Use synonyms or restructure sentences.
    """
)
st.write("**REMINDER**: Please do not use any outside tools (e.g., Google, ChatGPT) to assist you in this task. This is a test of your own ability to fool the AI.")


if st.button("Next"):
    st.switch_page("pages/experiment_intro_1_page.py")