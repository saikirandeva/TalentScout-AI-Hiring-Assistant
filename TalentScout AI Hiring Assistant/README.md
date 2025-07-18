# TalentScout AI Hiring Assistant

## Overview
An AI-powered chatbot that simulates the initial screening of job candidates for tech roles. Built with Streamlit and OpenAI's GPT-3.5/4, it collects candidate info, understands their tech stack, and generates personalized technical questions.

## Features
- Conversational UI (Streamlit)
- Collects candidate info: name, email, phone, location, experience, role, tech stack
- LLM-powered dynamic question generation
- Contextual memory for coherent chat
- Graceful handling of exits and invalid input
- No persistent storage; session-only data

## Setup
1. **Clone the repo**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API keys**:
   - Copy `.env.example` to `.env` and add your OpenAI API key
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## File Structure
```
app.py
requirements.txt
.env.example
prompts/
  info_collection.txt
  question_generation.txt
  fallback.txt
utils/
  llm.py
  prompts.py
  session.py
```

## Tech Stack
- Streamlit
- Python 3.8+
- OpenAI GPT-3.5/4

## License
MIT 