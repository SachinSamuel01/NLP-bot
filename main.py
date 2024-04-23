import streamlit as st
from sections.home import render_home
from sections.conversation import render_conversation

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'


# Check the current page and render it
if st.session_state.page == 'home':
    render_home()
elif st.session_state.page == 'conversation':
    render_conversation()
