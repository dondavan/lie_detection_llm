import streamlit as st

st.title("Specific Instructions and Information")
st.write("This page provides additional details and instructions to help you complete your task effectively.")

st.markdown(
    """
    ### Key Points:
    - **Understand the Task**: Your goal is to paraphrase statements to lower the AI's confidence in its classification.
    - **Maintain Meaning**: Ensure your paraphrases preserve the original meaning of the statement.
    - **Be Creative**: Use natural and grammatically correct language to rewrite the statements.
    - **Such Paraphrases Are Called Adversarial Examples**: Try to create paraphrases that confuse the AI into misclassifying the statement.

    ### Adversarial Example 
    - An adversarial example describes a change in the input data that causes a machine learning model to make a mistake.
    - Imagine a model classifying images of cats and dogs. By adding noise, such as changing individual pixels, you can trick the model into misclassifiying a cat as a dog. Importantly, the image still looks like a cat to you.
    - Models classifiying text can be similarly tricked by changing words or phrases in a statement while keeping the meaning, gramaticality, and naturalness intact. 
    - Meeting those criteria is important since changes in text will inevitably be visible to the human eye. To you such a rephrase should clearly say the same thing meaning that it is understandable to assume the classifier will make the same classification. However, in reality, the classifier might be tricked into making a different classification.
    - Example: ""I absolutely love this movie; it was a fantastic experience!" -> labeled as conveying a positive emotion.
    - Adversarial example: ""I truly adore this film; it was an incredible journey!" -> labeled as conveying a negative emotion. Means the same, is grammatically correct, and sounds natural. 
    ### Adversarial Paraphrase Example of a Deceptive Statment:
    - **Original Statement**: "XXX"
    - **Adversarial Paraphrase**: "XXX"
    ### Adversarial Paraphrase Example of a Truthful Statement:
    - **Original Statement**: "XXX"
    - **Adversarial Paraphrase**: "XXX"
    ### The Deception Classifer: 
    - Is an embedding-based model that was trained on a large dataset of truthful and deceptive statements. 
    - Embedding-based models learn to represent text by converting words into numbers, placing similar meanings closer together in a numerical space.
    - The model uses these representations to classify statements as truthful or deceptive. 
    - The model is more accurate than the average human in distinguishinh truth from lies.

    ### Tips:
    - Avoid simply reordering words; aim for meaningful changes.
    - Use synonyms or restructure sentences to make them appear different while keeping the meaning intact.
    """
)

if st.button("Next"):
    st.switch_page("pages/stepwise_training_page.py")