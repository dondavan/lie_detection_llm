import streamlit as st
import uuid

st.title("Informed Consent")

st.write("This study is conducted by researchers at Tilburg University and the University of Amsterdam (The Netherlands)")
st.write("Name and email address of the principal investigator: Dr Bennett Kleinberg, bennett.kleinberg@tilburguniversity.edu")
st.markdown(
"""
By proceeding, you voluntarily agree to participate in this study. 
This does not interfere with your right to withdraw from this study at any time without an explanation.

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
        st.session_state['prolific_id'] = st.query_params.get("PROLIFIC_PID", "no_prolific_id")
        
        if st.session_state['prolific_id'] == None :
            st.session_state['pid'] = str(uuid.uuid4())
        else:
            st.session_state['pid'] = st.session_state['prolific_id']

        st.session_state['store_data'] = 0
        st.session_state.consent_data = "Accepted"
        st.switch_page("pages/instructions_page.py")
with col3:
    if st.button("Deny"):
        st.session_state.consent_data = "Denied"
        st.switch_page("pages/end_page.py")