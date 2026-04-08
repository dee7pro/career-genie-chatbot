import html
import re
import streamlit as st
import base64

# -----------------------------
# Avatars
# -----------------------------
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

BOT_AVATAR = f"data:image/png;base64,{get_base64_image('ui/avatars/gemini_bot.png')}"
# Instead of ui/avatars/my_avatar.png
USER_AVATAR = f"data:image/png;base64,{get_base64_image('ui/avatars/trophy.png')}"  # Replace with any online image

# -----------------------------
# Helpers
# -----------------------------
def format_message(text):
    code_blocks = re.findall(r"```([\s\S]*?)```", text)
    text_blocks = re.split(r"```[\s\S]*?```", text)
    text_blocks = [html.escape(block) for block in text_blocks]

    formatted_text = ""
    for i in range(len(text_blocks)):
        formatted_text += text_blocks[i].replace("\n", "<br>")
        if i < len(code_blocks):
            formatted_text += f'<pre style="white-space: pre-wrap; word-wrap: break-word; background:#2d2d2d; color:#f8f8f2; padding:10px; border-radius:10px;"><code>{html.escape(code_blocks[i])}</code></pre>'
    return formatted_text

# -----------------------------
# Display Functions
# -----------------------------
def display_message(text, is_user=False):
    avatar = USER_AVATAR if is_user else BOT_AVATAR
    bubble_color = "#00B2FF" if is_user else "#71797E"
    align = "flex-end" if is_user else "flex-start"

    if is_user:
        message_html = f"""
        <div style="display:flex; align-items:flex-start; justify-content:{align}; margin-bottom:10px;">
            <div style="background:{bubble_color}; color:white; border-radius:20px; padding:10px; max-width:75%; font-size:14px; line-height:1.2; word-wrap:break-word;">
                {format_message(text)}
            </div>
            <img src="{avatar}" style="width:35px; height:35px; margin:5px; border-radius:50%;" />
        </div>
        """
    else:
        message_html = f"""
        <div style="display:flex; align-items:flex-start; justify-content:{align}; margin-bottom:10px;">
            <img src="{avatar}" style="width:35px; height:35px; margin:5px; border-radius:50%;" />
            <div style="background:{bubble_color}; color:white; border-radius:20px; padding:10px; max-width:75%; font-size:14px; line-height:1.2; word-wrap:break-word;">
                {format_message(text)}
            </div>
        </div>
        """
    st.write(message_html, unsafe_allow_html=True)

def display_streaming_message(tokens, placeholder):
    message_text = "".join(tokens)
    escaped_text = html.escape(message_text).replace('\n', '<br>')
    message_html = f"""
    <div style="display:flex; align-items:flex-start; justify-content:flex-start; margin-bottom:10px;">
        <img src="{BOT_AVATAR}" style="width:35px; height:35px; margin:5px; border-radius:50%;" />
        <div style="background:#71797E; color:white; border-radius:20px; padding:10px; max-width:75%; font-size:14px; line-height:1.2; word-wrap:break-word;">
            {escaped_text}
        </div>
    </div>
    """
    placeholder.markdown(message_html, unsafe_allow_html=True)