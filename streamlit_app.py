import streamlit as st
from gemini_ai import create_gemini_ai
from dotenv import load_dotenv

load_dotenv()

# Initialize session state
if 'gemini' not in st.session_state:
    st.session_state.gemini = create_gemini_ai()
if 'history' not in st.session_state:
    st.session_state.history = []

# UI Configuration
st.title(" CN🤍 AI ")

# Background Image URL
background_image_url = "https://i.postimg.cc/FKFZgMWB/Obituary.jpg"

# Apply Full-Screen Background Image
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_image_url}") no-repeat center center fixed;
        background-size: cover;
        height: 100vh;
        width: 100vw;
        position: absolute;
        top: 0;
        left: 0;
        z-index: -1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display chat history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask CN🤍...")

if user_input:
    # Add user message to history
    st.session_state.history.append({"role": "user", "content": user_input})

    # Get response
    with st.spinner('YOUR CN🤍 is thinking...'):
        response = st.session_state.gemini.invoke(user_input)

    # Add AI response to history
    st.session_state.history.append({
        "role": "assistant",
        "content": response['response']
    })

    # Refresh display
    st.rerun()
