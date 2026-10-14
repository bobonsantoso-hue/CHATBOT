import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="StudyBuddy", page_icon="📚", layout="centered")

@st.cache_resource
def init():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

client = init()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("📚 StudyBuddy")
st.caption("Your AI Learning Companion")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                messages = [{"role": "system", "content": "You are StudyBuddy, a friendly AI tutor. Be encouraging and clear."}]
                for m in st.session_state.messages:
                    messages.append({"role": m["role"], "content": m["content"]})
                
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=800
                )
                
                bot_response = response.choices[0].message.content
                st.write(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Error: {str(e)}")
