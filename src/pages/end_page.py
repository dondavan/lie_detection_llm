import streamlit as st

st.title("End of Study")
st.write("Thank you for participanting in our study.")
st.subheader("Debriefing")
st.write(
    """This study investigated how humans (you) modify statements in a live human-AI interaction.

We will compare these human modifications with modifications done by a large language model to understand how an AI model can best be misled. Consequently, we aim to use these insights to develop more secure and robust AI classification systems."""
)
st.write("Thank you for your valuable contribution.")
st.write("You will now be redirected to Prolific.")

if st.button("Return to Prolific"):
        prolific_home_url = "https://app.prolific.com/submissions/complete?cc=C166MB7Y"
        st.markdown(f"<a href='{prolific_home_url}' target='_blank'>Click here if you're not automatically redirected</a>", unsafe_allow_html=True)