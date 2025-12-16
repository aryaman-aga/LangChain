import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
langchain_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_key

st.title("Langchain Demo With LLAMA2 API")

# Note: Make sure Ollama application is running on your Mac
try:
    llm = Ollama(model="llama3.1:8b")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Please response to the user queries with concise answers. If you don't know the answer, just say that you don't know."),
            ("user", "Question:{question}")
        ]
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    input_text = st.text_input("Search the topic u want")

    if input_text:
        with st.spinner("Thinking..."):
            st.write(chain.invoke({"question": input_text}))

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.warning("Please ensure the Ollama application is running and the 'llama2' model is installed (`ollama pull llama2`).")
