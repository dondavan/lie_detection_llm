import streamlit as st

st.title("End of Study")
st.write("Thank you for participanting in our study. You have exited the study.")
st.subheader("Debriefing")
st.write("""This study investigated how robust automated deception classifiers are to rewrites of the original statements. 
        These rewrites will be fed into the AI to investigate how its performance differs from the original statements.
        Further, we will investigate how people constructed these paraphrases. 
        If you have any questions, feel free to contact us at:  
        bennett.kleinberg@tilburguniversity.edu """)
st.write("Thank you for your valuable contribution.")
st.write("You will now be redirected to Prolific.")

if st.button("Return to Prolific"):
        prolific_home_url = "https://app.prolific.com/submissions/complete?cc=C166MB7Y"
        st.markdown(f"<a href='{prolific_home_url}' target='_blank'>Click here if you're not automatically redirected</a>", unsafe_allow_html=True)