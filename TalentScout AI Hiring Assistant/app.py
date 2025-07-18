import streamlit as st
from utils.llm import get_llm_response
from utils.prompts import load_prompt
from utils.session import get_session_state

st.set_page_config(page_title="TalentScout AI Hiring Assistant", page_icon="🤖")
st.title("TalentScout AI Hiring Assistant 🤖")

# Info fields to collect in order
INFO_FIELDS = [
    ("name", "What is your full name?"),
    ("email", "What is your email address?"),
    ("phone", "What is your phone number?"),
    ("location", "Where are you located? (City, Country)"),
    ("experience", "How many years of professional experience do you have?"),
    ("role", "What is your desired role or position?"),
    ("tech_stack", "Please list your main programming languages, tools, and frameworks (comma-separated)."),
]

state = get_session_state()

# Initialize chat history if not present
if not state['chat_history']:
    greeting = "Hello! I'm TalentScout, your AI hiring assistant. Let's get started with a few questions."
    state['chat_history'].append(("assistant", greeting))
    state['current_field'] = 0
    state['candidate_data'] = {}

# Display chat history
for sender, message in state['chat_history']:
    if sender == "assistant":
        st.markdown(f"**🤖 TalentScout:** {message}")
    else:
        st.markdown(f"**🧑 You:** {message}")

# Check if all info is collected
if state.get('current_field', 0) < len(INFO_FIELDS):
    key, prompt = INFO_FIELDS[state['current_field']]
    user_input = st.text_input("Your response:", key="user_input")
    if st.button("Send") and user_input.strip():
        # Save user response
        state['chat_history'].append(("user", user_input.strip()))
        state['candidate_data'][key] = user_input.strip()
        state['current_field'] += 1
        # Next assistant prompt
        if state['current_field'] < len(INFO_FIELDS):
            next_prompt = INFO_FIELDS[state['current_field']][1]
            state['chat_history'].append(("assistant", next_prompt))
        st.experimental_rerun()
else:
    st.success("Thank you! All your information has been collected. (Technical question generation coming next.)")
    st.write("**Summary of your info:**")
    for k, v in state['candidate_data'].items():
        st.write(f"- **{k.capitalize()}**: {v}") 