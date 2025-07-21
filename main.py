import os
import streamlit as st
from constants import gemini_key
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

# Set API key
os.environ["GOOGLE_API_KEY"] = gemini_key

# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="Famous People Explorer", page_icon="🌟")
st.title("🌟 Famous People Explorer")
st.markdown(
    """
    🔍 **Discover facts, movies, and historical events related to your favorite celebrities, athletes, or public figures.**  
    Enter a name and let Gemini Flash + LangChain do the magic!
    """
)
input_text = st.text_input("Enter the name of a famous person:")

# -------------------- Memory Buffers --------------------
person_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
info_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")
event_memory = ConversationBufferMemory(input_key="info", memory_key="description_history")

# -------------------- Prompt Templates --------------------
first_input_prompt = PromptTemplate(
    input_variables=["name"],
    template="Briefly introduce the celebrity {name} in around 100 words."
)

second_input_prompt = PromptTemplate(
    input_variables=["person"],
    template="""
    If {person} is an actor, list 3 popular movies.  
    If a sportsperson, mention their favorite food.  
    Otherwise, suggest 1-2 favorite travel destinations. (Keep within 100 words)
    """
)

third_input_prompt = PromptTemplate(
    input_variables=["info"],
    template="List 5 famous global events related to {info}, each within 10 words."
)

# -------------------- Google Gemini LLM --------------------
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    temperature=0.8
)

# -------------------- Chains --------------------
chain1 = LLMChain(llm=llm, prompt=first_input_prompt, output_key="person", memory=person_memory, verbose=True)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, output_key="info", memory=info_memory, verbose=True)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, output_key="events", memory=event_memory, verbose=True)

# -------------------- Sequential Chain --------------------
chain_combine = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=["name"],
    output_variables=["person", "info", "events"],
    verbose=True
)

# -------------------- Run the Chain --------------------
if st.button("🔍 Search") and input_text:

    with st.spinner("🔎 Searching..."):
        try:
            response = chain_combine.invoke({"name": input_text})
            st.subheader("👤 About the Person")
            st.write(response["person"])
            st.subheader("🎬 Movies / 🍽️ Food / 🌍 Places")
            st.write(response["info"])
            st.subheader("📅 Famous Events")
            st.write(response["events"])
        except Exception as e:
            st.error(f"🚫 Error: {str(e)}")
