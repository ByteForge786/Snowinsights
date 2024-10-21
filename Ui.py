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

    # Initialize chat history and user input
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Initial greeting and suggested questions
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown("Hi! I'm your mock LLM chatbot. How can I help you today?")
            st.markdown("Here are some suggested questions you can ask:")
            suggested_questions = get_suggested_questions()
            cols = st.columns(len(suggested_questions))
            for idx, question in enumerate(suggested_questions):
                if cols[idx].button(question, key=f"suggest_{question}"):
                    st.session_state.user_input = question
                    st.rerun()
            st.markdown("Feel free to ask any of these questions or type your own!")
        
        greeting = "Hi! I'm your mock LLM chatbot. How can I help you today?\n\nHere are some suggested questions you can ask:\n"
        greeting += "\n".join([f"- {q}" for q in suggested_questions])
        greeting += "\n\nFeel free to ask any of these questions or type your own!"
        st.session_state.messages.append({"role": "assistant", "content": greeting})

    # Chat input
    user_input = st.chat_input("What's your question?", key="chat_input")

    # If there's a stored user input, use it and clear the storage
    if st.session_state.user_input:
        user_input = st.session_state.user_input
        st.session_state.user_input = ""

    if user_input:
        # Display user message in chat message container
        st.chat_message("user").markdown(user_input)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = get_mock_response(user_input)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Rerun the app to display the new messages
        st.rerun()

if __name__ == "__main__":
    chat_interface()
