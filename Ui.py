import streamlit as st
from typing import List

def get_mock_response(user_input: str) -> str:
    responses = {
        "Hello": "Hello! How can I assist you today?",
        "How are you?": "As an AI, I don't have feelings, but I'm functioning well and ready to help!",
        "What's the weather like?": "I'm sorry, I don't have access to real-time weather data. You might want to check a weather app or website for accurate information.",
        "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    }
    return responses.get(user_input, "I'm not sure how to respond to that. Can you please rephrase or ask something else?")

def get_suggested_questions() -> List[str]:
    return [
        "Hello",
        "How are you?",
        "What's the weather like?",
        "Tell me a joke"
    ]

def chat_interface():
    st.title("Mock LLM Chatbot")

    # Initialize chat history, suggestions, and user input
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "show_suggestions" not in st.session_state:
        st.session_state.show_suggestions = True

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Show suggestions initially
    if st.session_state.show_suggestions:
        with st.chat_message("assistant"):
            st.markdown("Hi! I'm your mock LLM chatbot. How can I help you today?")
            st.markdown("Here are some suggested questions you can ask:")
            suggested_questions = get_suggested_questions()
            cols = st.columns(len(suggested_questions))
            for idx, question in enumerate(suggested_questions):
                if cols[idx].button(question, key=f"suggest_{question}"):
                    # Add question and response to chat history
                    st.session_state.messages.append({"role": "user", "content": question})
                    response = get_mock_response(question)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                    # Remove suggestions after a question is selected
                    st.session_state.show_suggestions = False

    # Chat input for user to ask their own questions
    user_input = st.chat_input("What's your question?", key="chat_input")
    
    if user_input:
        # Display user message in chat message container
        st.chat_message("user").markdown(user_input)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get response and add to chat history
        response = get_mock_response(user_input)
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    chat_interface()
