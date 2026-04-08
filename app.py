import streamlit as st
from backend.gemini_client import get_client, create_chat_session
from backend.chatbot import get_response
from backend.prompts import get_system_prompt
from ui.chat_ui import display_message

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Career Advisor Chatbot")

# -----------------------------
# Gradient Title
# -----------------------------
gradient_text_html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700;900&display=swap');

.career-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 900;
  font-size: 4em;
  background: linear-gradient(90deg, #FF4E50, #F9D423);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
  margin: 0;
  padding: 20px 0;
  text-align: center;
}
</style>
<div class="career-title">CareerGenie</div>
"""
st.markdown(gradient_text_html, unsafe_allow_html=True)
st.caption("Your AI Career Advisor")

# -----------------------------
# Initialize session state
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm CareerGenie, your AI career advisor. Ask me anything about AI careers!"}
    ]

if "client" not in st.session_state:
    st.session_state.client = get_client()

if "chat_session" not in st.session_state:
    st.session_state.chat_session = create_chat_session(
        st.session_state.client,
        get_system_prompt()
    )

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("## ⚙️ CareerGenie Controls")

    topics = ["Resume Tips", "AI Internships", "Interview Prep", "Job Search Strategies"]
    selected_topic = st.selectbox("Select a topic:", options=topics)

    st.markdown(f"**Selected Topic:** {selected_topic}")

    if st.button("Reset Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm CareerGenie, your AI career advisor. Ask me anything about AI careers!"}
        ]
        st.rerun()


    st.divider()

    st.markdown("### About CareerGenie")
    st.markdown(
        """
- 🎯 Roadmaps  
- 💼 Internships  
- 🛠️ Projects  
- 🎤 Interview Prep  

⚡ From beginner → job-ready in AI
"""
    )
# -----------------------------
# Display chat messages
# -----------------------------
for msg in st.session_state.messages:
    display_message(msg["content"], is_user=(msg["role"] == "user"))

# -----------------------------
# User input
# -----------------------------
user_input = st.chat_input("Ask about AI careers...")
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    display_message(user_input, is_user=True)

    # Generate AI response
    with st.spinner("Thinking..."):
        reply = get_response(st.session_state.chat_session, user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    display_message(reply, is_user=False)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='font-size:13px; text-align:center;'> Developed by <b>deepika </b></p>",
    unsafe_allow_html=True
)
