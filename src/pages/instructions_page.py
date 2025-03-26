import streamlit as st

st.title("Instructions")
st.write(":book: In this experiment, you will read **XXX** short statements about past experiences. Each statement is either truthful :white_check_mark: or a lie :lying_face:.")
st.write("Your task is to paraphrase these statements to deceive an machine-learning-based lie detection classifier. Specifically, you'll rewrite the statements while maintaining their original meaning, grammatical correctness, and naturalness, aiming to mislead the classifier into incorrectly labeling them as truthful or deceptive (depending on their initial credibility).")
st.write("A natural rewrite preserves fluency, readability, and coherence.")
st.write("These statements were randomly selected from a larger dataset in which half of all statements are truthful, and half of them are lies.")

st.write("""To help you with your task, we provide you with the predictions of a state-of-the-art lie detection algorithm based on artificial intelligence (AI) :robot_face:
            This algorithm shows better performance in distinguishing truth from lies than the average human.""")
st.write("You will receive feedback showing how confident the AI is in its classification after each rewrite. Your goal is to maximize the change in the AI's confidence score (lower the percentage shown for the initial statement) through your paraphrases.")
st.write("The feedback is shown in terms of a percentage that the statement belongs to either for the target categories (lie or truth). 0 percent indicates low confidence, while 100 percent indicates high confidence.")
st.write("In total you will have 10 attempts to change the confidence score as much as possible. If you manage to lower the initial confidence shown (percentage) to lower than 50 percent, you will be instructed to move on to the next statement.")
st.write("You'll undergo a guided training procedure to make you familiar with the task and will be provided with examples on the next pages.")

st.write("**Please note that you should read and paraphrase the statements carefully, as after the task you will have to take a quick quizz. The quiz serves to validate your participation.**")

if st.button("Next"):
    st.switch_page("pages/specific_instructions_page.py")