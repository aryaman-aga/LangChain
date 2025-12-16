import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from constants import groq_key

if groq_key:
    os.environ["GROQ_API_KEY"] = groq_key

st.title("LangChain Demo (celebrity edition)")
input_text = st.text_input("Enter your query")

# Initialize LLM
llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.3
)


# Prompt
first_prompt = PromptTemplate(
    input_variables=["name"],
    template="Who is {name}?"
)

second_prompt = PromptTemplate(
    input_variables=["content"],
    template="Based on the following information, when was this person born and what are they known for?\n{content}"
)

chain = first_prompt | llm | second_prompt | llm


if st.button("Generate"):
    result = chain.invoke({"name": input_text})
    st.markdown(result.content)

# Note: Avoid printing the API key or any sensitive information
