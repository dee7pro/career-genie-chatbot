# Career Genie — Production-Ready GenAI Chatbot

🚀 **Career Genie** is a Generative AI-powered chatbot designed to guide students and professionals in AI careers. Get personalized advice on internships, skill-building, job search strategies, and roadmap planning — all in one chat interface.  

---

## Screenshots

<div style="display:flex; gap:10px; flex-wrap:wrap;">
  <img width="300" alt="Screenshot 1" src="" />
  <img width="300" alt="Screenshot 2" src="" />
  <img width="300" alt="Screenshot 3" src="" />
</div>

---

## Features

- 💬 AI-powered career advisor specializing in Generative AI  
- 📝 Personalized advice on internships, skills, and career roadmap  
- ⚡ Real-time chat interface built with **Streamlit**  
- 🔒 Supports secure API keys via `.env` or **Streamlit Secrets**  
- 🖥️ Sidebar for quick topic selection: Resume Tips, AI Internships, Interview Prep, Job Search  

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | gemini-3-flash-preview |
| Framework | LangChain |
| UI | Streamlit |

--- 

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/dee7pro/career-genie-chatbot.git
cd career-genie-chatbot
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add API Key**

Create a `.env` file:
```
gemini_class = your_gemini_api_key_here
```

**5. Run**
```bash
streamlit run app.py

```

## Sidebar Features

- Select topics: Resume Tips, AI Internships, Interview Prep, Job Search Strategies
- Reset chat button to start a new session

---

## Example Questions for Career Genie

- How can I land a Generative AI internship?
- Which skills should I prioritize for AI/ML roles?
- What roadmap should I follow to become a prompt engineering expert?
- How to prepare for AI job interviews?
- Which online resources or certifications are most valuable in 2026?
