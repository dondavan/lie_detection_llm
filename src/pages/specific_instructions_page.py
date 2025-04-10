import streamlit as st

st.title("Key Points")
st.write("This page refreshes the key points that are important for this task.")

st.markdown(
    """
    ### Key Points:
    - **Understand the Task**: Your goal is to paraphrase statements to lower the AI's confidence in its classification.
    - **Maintain Meaning**: Ensure your paraphrases preserve the original meaning of the statement.
    - **Use of Language**: Use natural and grammatically correct language to rewrite the statements.
    - **Overall**: Try to create paraphrases that confuse the AI into misclassifying the statement.
    - **Tips**: Avoid simply reordering words; Use synonyms or restructure sentences while keeping the meaning intact.
    """
)

if st.button("Next"):
    st.switch_page("pages/stepwise_training_page.py")