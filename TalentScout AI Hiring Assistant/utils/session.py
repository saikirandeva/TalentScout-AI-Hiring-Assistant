import streamlit as st

def get_session_state():
    if 'candidate_data' not in st.session_state:
        st.session_state['candidate_data'] = {}
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    return st.session_state 