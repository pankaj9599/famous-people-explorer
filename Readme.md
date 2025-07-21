# 🌟 Famous People Explorer

A simple and smart web app built using **Streamlit**, **LangChain**, and **Google Gemini 1.5 Flash**, that helps you discover quick and interesting facts about famous personalities.

---

## 🔍 Features

- 🔎 Search any **famous person** (celebrity, actor, athlete, etc.)
- 🤖 Get a **100-word bio** about the person
- 🎬 Suggests:
  - 3 movies if they are an actor
  - Favorite food if a sportsperson
  - Travel destinations otherwise
- 📅 Lists 5 historical/global events related to them
- 💬 Powered by **LangChain SequentialChain + Gemini Flash**

---

## 🛠️ Tech Stack

- Python 🐍
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)

---

## 📁 Project Structure
search_persons/
├── myenv/ # Virtual environment (ignored)
├── constants.py # Contains your Gemini API key (not uploaded)
├── main.py # Streamlit app
├── requirements.txt # All dependencies
└── README.md # This file
