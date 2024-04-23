import os
import streamlit as st
from streamlit_lottie import st_lottie
import json  # Import json module for loading local JSON files
from lib.audio_recorder import record_until_silence
from lib.run_whisper import transcribe_audio
from lib.response import tts_response
from lib.llm import bot

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idle_path = os.path.join(base_path, 'assets', "idle.json")
recording_path = os.path.join(base_path, 'assets', "recording.json")
output_path = os.path.join(base_path, 'assets', "response.json")

def set_st_container(container, path, text, key_suffix):
    # Create columns for centering content
    container.empty()
    col1, col2, col3 = container.columns([1,2,1])
    with col2: 
        st.markdown(f"""
        <div class="center-container">
            <div>{st_lottie(load_lottiefile(path), height=300, key=f"lottie_{key_suffix}")}</div>
            <p>{text}</p>
        </div>
        """, unsafe_allow_html=True)

def load_lottiefile(filepath: str):
    """Load a Lottie file from the specified filepath."""
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def set_chat(container, text):
    container.empty() 
    container.markdown(f"<p style='word-wrap: break-word; white-space: normal;'>{text}</p>", unsafe_allow_html=True)

def render_conversation():
    st.title('Start Conversation')
    st.markdown("---")
    
    audio_container = st.empty()


    # Inject custom CSS through markdown for centering content
    st.markdown("""
    <style>
    .center-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;  # Stack items vertically
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize or use existing session state for recording
    if 'audio_mode' not in st.session_state:
        st.session_state.audio_mode = "idle"
    
    if 'question' not in st.session_state:
        st.session_state.question = ""
    
    if 'response' not in st.session_state:
        st.session_state.response = ""

    set_st_container(audio_container, idle_path, "Click 'Ask Button' to speak...", "idle")

    # Position the button before the text placeholders
    ask_question_button = st.button('Ask Question')

    # Initialize placeholders after the button
    question_container = st.empty()
    response_container = st.empty()

    set_chat(question_container, st.session_state.question)
    set_chat(response_container, st.session_state.response)
    # Add a button to manually set the recording state to True
    if ask_question_button:
        if st.session_state.audio_mode == "idle":
            set_chat(question_container, "")
            set_chat(response_container, "")

            st.session_state.audio_mode = "recording"
            set_st_container(audio_container, recording_path, "Start speaking...", "recording")
            base_path = os.path.abspath(os.path.dirname(__file__))
            parent_path = os.path.dirname(base_path)
            recordings_path = os.path.join(parent_path, 'recordings')
            audio_path = record_until_silence(recordings_path)
            st.session_state.audio_mode = "idle"
            set_st_container(audio_container, idle_path, "Processing...", "processing")

            stt = transcribe_audio(audio_path)
            set_chat(question_container, "Question: " + stt)
            st.session_state.question = "Question: " + stt

            response = bot(st.session_state.prompt, stt, st.session_state.files[0])
            set_chat(response_container, "Response: " + response)
            st.session_state.response = "Response: " + response

            os.remove(audio_path)
            st.session_state.audio_mode = "response"
            set_st_container(audio_container, output_path, "Response...", "response")
            tts_response(response, st.session_state.voice)
            set_st_container(audio_container, idle_path, "Processing...", "processing2")
            st.session_state.audio_mode = "idle"
            st.rerun()

    question_container = st.empty()
    response_container = st.empty()

    # Back button
    if st.button('Back'):
        st.session_state.page = 'home'
        st.session_state.audio_mode = "idle"
        st.session_state.question = ""
        st.session_state.response = ""
        st.rerun()

