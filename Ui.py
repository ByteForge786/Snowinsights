import streamlit as st
from typing import List, Tuple
import random
import time

# Mock LLM response function
def get_llm_response(prompt: str) -> str:
    # Simulate API call delay
    time.sleep(1.5)
    responses = [
        "Based on the latest research, it appears that...",
        "That's an interesting question. In my analysis...",
        "There are several factors to consider here...",
        "According to recent studies in this field...",
        "While opinions vary, the consensus among experts is..."
    ]
    return random.choice(responses) + " " + prompt

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

def display_message(role: str, content: str):
    with st.chat_message(role):
        st.markdown(content)

def display_suggested_questions():
    st.markdown("Here are some questions you might want to ask:")
    questions = [
        "📊 What are the latest trends in data science?",
        "🌐 How is AI impacting global economics?",
        "🧠 Can you explain the concept of neural networks?",
        "🚀 What advancements are happening in space exploration?",
        "🌿 How can technology contribute to environmental sustainability?"
    ]
    for question in questions:
        if st.button(question):
            st.session_state.user_input = question

# Main application
st.title("💬 Professional AI Assistant")

# Display chat history
for message in st.session_state.messages:
    display_message(message["role"], message["content"])

# Initial greeting
if not st.session_state.messages:
    display_message("assistant", "👋 Hello! I'm your AI assistant. How can I help you today?")
    display_suggested_questions()

# User input
user_input = st.chat_input("Type your message here...", key="user_input", value=st.session_state.user_input)
if user_input:
    # Clear the session state user input
    st.session_state.user_input = ''
    
    # Display user message
    display_message("user", user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get and display AI response
    ai_response = get_llm_response(user_input)
    display_message("assistant", ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Force a rerun to display the new messages immediately
    st.experimental_rerun()

# Sidebar for additional options
with st.sidebar:
    st.title("⚙️ Chat Options")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.experimental_rerun()
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    This AI assistant is powered by advanced language models and is designed to provide informative and engaging responses on a wide range of topics.
    
    Please note that while our AI strives for accuracy, it may occasionally provide incorrect information. Always verify critical information from authoritative sources.
    """)
