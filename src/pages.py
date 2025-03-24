import streamlit as st
import time
import datetime
#import gspread
import pandas as pd 
import random
import uuid 
#from deta import Deta as Dt
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import time
import numpy as np
import os

# Define progress bar
total_steps = 22

def update_progress():
     if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
     if st.session_state.current_step < total_steps:
         st.session_state.current_step += 1

def show_progress_bar():
    if 'current_step' in st.session_state:
        progress = st.session_state.current_step / total_steps
        st.progress(progress)
    else:
        st.session_state.current_step = 0
        st.progress(0)
        
def welcome_page(): 
    show_progress_bar()

    st.title("Welcome to the _'ADVERSARIAL PARAPHRASING ATTACKS ON AUTOMATED DECEPTION CLASSIFIERS'_ study")
    st.write("""This study explores how robust automated deception classifiers are to modifications - paraphrases - to a statement they classify. 
             After you have consented to participate in this experiment, we will give you detailed instructions. **Please read them carefully.**
             \nOnce you complete the experiment, you will be redirected to Prolific.""")
    
    if st.button("Next"):
        update_progress()
        st.session_state.page = 'consent'
    

def consent_page():
    show_progress_bar()

    st.title("Informed Consent")

    st.write("This study is conducted by researchers at Tilburg University and the University of Amsterdam (The Netherlands)")
    st.write("Name and email address of the principal investigator: Dr Bennett Kleinberg, bennett.kleinberg@tilburguniversity.edu")
    st.markdown(
    """
    The study was reviewed and approved by the university’s ethics committee.
    Please proceed if you agree to the following:

    - I confirm that I have read and understood the information provided for this study.
    - I understand that my participation is voluntary.
    - I understand that I remain fully anonymous, and that I will not be identifiable in any publications or reports on the results of this study.
    - I understand that the data collected in this survey might be made publicly available. I know that no personal information whatsoever will be included in this dataset and that my anonymous research data can be stored for the period of 10 years.
    - I understand that the results of this survey will be reported in academic publications or conference presentations.
    - I understand that I will not benefit financially from this study or from any possible outcome it may result in in the future.
    - I understand that I will be compensated for participation in this study as detailed in the task description on Prolific.
    - I am aware of who I should contact if I wish to lodge a complaint or ask a question.
    """, 
    unsafe_allow_html=True)

    st.write("""Please click on "Accept" if you want to give your consent and proceed with the experiment.
              Otherwise, click  on "Deny" and the experiment ends.""")
    
    col1, col2, col3 = st.columns([2,6,2])
    with col1:
        if st.button("Accept"):
            st.session_state.consent_data = "Accepted"
            update_progress()
            st.session_state.page = 'instructions'
    with col3:
        if st.button("Deny"):
            st.session_state.consent_data = "Denied"
            update_progress()
            st.session_state.page = 'end'

def instructions_page():
    show_progress_bar()

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
        update_progress()
        st.session_state.page = 'specific_instructions' 

def specific_instructions_page():
    show_progress_bar()

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
        update_progress()
        st.session_state.page = 'stepwise_training'

def stepwise_training_page():
    show_progress_bar()

    st.title("Training Procedure")
    st.write("You will now perform four subtasks as part of a stepwise training procedure to familiarize yourself with the task.")

    if st.button("Next"):
        update_progress()
        st.session_state.page = 'experiment'

def experiment_page():
    show_progress_bar()
    
    st.title("LLM based Verbal Lie Detection")
    #st.markdown("Instructions for use:") 
    #st.markdown("▶  Write a short story which can either be true or false.")
    #st.markdown("▶  The system will attempt to evaluate the truthfulness of the input, by giving a credibility score (probability).")
    #obj = '<p style="color:#06b0db; font-size: 20px; fond-weight: bold;">Try to fool the system by finding an adversarial example</p>'
    #st.markdown(obj, unsafe_allow_html=True)

    def load_statements():
        return pd.read_csv("../data/hippocorpus_test_set.csv", sep=";")
    
    # Load statements and select a random one
    statements = load_statements()
    random_statement = statements.sample(n=1).iloc[0]
    statement_text = random_statement['text']
    condition_1 = random_statement['condition']
    if condition_1 is "truthful":
        condition_2 = "deceptive"
    else:
        condition_2 = "truthful"

    # Display the statement and instructions
    st.write(f"This is a {condition_1} statement. Rewrite this statement so that it appears {condition_2} to an automated deception classifier. Please maintain the original meaning of the statement, ensure grammaticality, and that your rewrite appears natural.")
    st.write(f"Original statement: {statement_text}")

    desc = st.markdown("Write your text below:")
    
    ans_container = st.empty()
    input_container = st.empty()
    submit_cont = st.empty()
    progr_cont = st.empty()
    up_button_cont = st.empty()
    down_button_cont = st.empty()
    
    def chatloop(frase):
        tokenize = tokenizer(frase, return_tensors='tf')
        for i in [tokenize]:
            h = model.generate(**i)
            decoded_pred = tokenizer.batch_decode(h, skip_special_tokens=True)
            h1 = model.generate(**i, return_dict_in_generate=True, output_scores=True)
            prob = np.max(np.exp(h1.scores)/np.sum(np.exp(h1.scores)))
        return decoded_pred[0], prob

    def generate(input_txt, index):
        risposta, sicurezza = chatloop(frase=str(input_txt))
        prob = str(sicurezza)[2] + str(sicurezza)[3]
        prob = int(prob)
        submit_cont.empty()
        input_container.empty()

        if risposta == "T":
            desc.markdown("The paragraph is true. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(prob))
            up_button = up_button_cont.button("CORRECT", key=index+500, args=(input_txt,risposta,True,index))
            down_button = down_button_cont.button("WRONG", key=-(index + 500), args=(input_txt, risposta, False, index))
            progr_cont.progress(prob)
        elif risposta == "F":
            desc.markdown("The paragraph is false. The credibility score is {}%, represented by the coloured bar below. Please evaluate whether the classification is wrong or correct.".format(prob))
            up_button = up_button_cont.button("CORRECT", key=(index+5)*500, args=(input_txt, risposta, True, index))
            down_button = down_button_cont.button("WRONG", key=-(index+5)*500, args=(input_txt, risposta, False, index))
            progr_cont.progress(prob)
        
        time.sleep(3)
        load(j=index)

    def load(j):
        j+=1

        input_container.empty()
        progr_cont.empty()
        ans_container.empty()
        up_button_cont.empty()
        down_button_cont.empty()
        
        input = input_container.text_area("Enter your rewritten statement here", key=j, label_visibility="collapsed")
        submit_butt = submit_cont.button("SUBMIT", key=-j)
        if submit_butt:
            generate(input, j)
    
    load(j=0)
    for i in range (0,8):
        st.text("")

    #st.session_state.statement = st.text_area("Statement")

    #if st.button("Submit"):
     #   update_progress()
      #  data = [st.session_state.statement]
       # st.session_state.page = "end"
        #st.experimental_rerun()
    

def feedback_page():
    show_progress_bar()
    
    st.title("Feedback")
    st.write("Please provide us with feedback about the study. Your feedback is valuable to us and will help us improve our study.")
    
    st.write("**1. How much were you motivated to perform well?**")
    st.session_state.motivation_scale = st.slider("0 = Not at all, 10 = Very much", min_value=0, max_value=10, value=5, step=1)

    st.write("**2. How difficult did you find the study?**")
    st.session_state.difficulty_scale = st.slider("0 = Very easy, 10 = Very difficult", min_value=0, max_value=10, value=5, step=1)
    
    st.write("What strategies did you use to complete the task and flip the classification label?")
    st.session_state.strategies = st.text_area("Strategies")

    st.write("Optionally, you can leave any remarks or feedback you have about this experiment. Please click on the button below to submit your feedback.")
    st.session_state.feedback = st.text_area("Feedback")
   
    if st.button("Submit Feedback"):
        update_progress()
        feedback_data = [
            st.session_state.like_scale,
            st.session_state.difficulty_scale,
            st.session_state.feedback]
        
        # Retrieve response_data and questions_data from session state
        questions_data = st.session_state.questions_data
        
        # Concatenate all data into a single list
        combined_data =  questions_data + feedback_data 
       # submit_to_sheet_2(combined_data)
        st.write("Thank you for your feedback.")
        st.session_state.page = 'end'

def end_page():
    update_progress()
    show_progress_bar()
    st.title("End of Study")
    st.write("Thank you for participanting in our study. You have exited the study.")
    st.subheader("Debriefing")
    st.write("""This study investigated how people rely on AI judgments. 
            However, for this experiment the AI predictions were fictitious, meaning that we didn't train any model.
            We just manipulated the levels of accuracy and confidence to define at which point humans align the most with AI judgments. 
            If you have any questions, feel free to contact us at:  
            bennet.kleinberg@tilburguniversity.edu  
            r.loconte@tilburguniversity.edu""")
    st.write("Thank you for your valuable contribution.")