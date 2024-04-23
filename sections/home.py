import streamlit as st
import time  # To simulate a delay

# Function to simulate API setup and processing
def setup_api():
    time.sleep(3)  # Simulate time taken to set up API

# Page rendering logic
def render_home():
    st.title('Natural Language Conversation Bot')
    st.markdown("---")

    bot_name = st.text_input("Write the name of the bot:")
    voice_options = ['Male', 'Female']
    selected_voice = st.selectbox("Select the voice of the character:", voice_options)
    user_prompt = st.text_area("Write the persona and character features:", height=150)
    uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type='txt')

    if st.button('Start Conversation'):
        with st.spinner('Setting up... Please wait.'):
            st.session_state.voice = selected_voice
            st.session_state.name = bot_name
            st.session_state.prompt = user_prompt
            print(uploaded_files)
            st.session_state.files = uploaded_files
            setup_api()  # Simulate setting up APIs like OpenAI Whisper
        st.session_state.page = 'conversation'
        st.rerun()
