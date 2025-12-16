from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn 
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    version="1.0.0",
    description= "API server for LangChain models ( simple server )"
)

groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise RuntimeError("GROQ_API_KEY not found. Check your .env file.")

model = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.3,
    api_key=groq_key
)

add_routes(
    app,
    model,
    path="/groq"  
)

llm = Ollama(model="llama3.1:8b")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 50 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 1000 words")

add_routes(
    app,
    prompt1|llm| StrOutputParser(),
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)



