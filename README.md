# LangChain Playground

A small collection of LangChain demos:
- FastAPI + LangServe endpoints powered by Groq and Ollama ([api/app.py](api/app.py))
- Streamlit clients for the API ([api/client.py](api/client.py)) and Groq/Ollama playgrounds ([chatbot/main.py](chatbot/main.py), [chatbot/localllm.py](chatbot/localllm.py))
- A LangGraph ReAct agent notebook with Wikipedia/Arxiv/LangSmith tools ([agents/agents.ipynb](agents/agents.ipynb))

## Prerequisites
- Python 3.10+ (virtual env recommended)
- Groq API key (create a free key at https://console.groq.com/keys)
- Optional: Ollama running locally with the model `ollama pull llama3.1:8b` (needed for embeddings in the notebook and the Ollama endpoints)
- Optional: LangSmith/LangChain API key for tracing

## Setup
1) Clone and enter the repo
```bash
git clone https://github.com/<your-username>/LangChain.git
cd LangChain
```
2) Create & activate a virtualenv
```bash
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
# .venv\\Scripts\\activate  # on Windows
```
3) Install dependencies
```bash
pip install -r requirements.txt
```
4) Environment variables (create a `.env` file in the project root)
```
GROQ_API_KEY=your_groq_key
LANGCHAIN_API_KEY=optional_langsmith_key
LANGCHAIN_TRACING_V2=true
```
Ollama users: ensure `ollama serve` is running and the `llama3.1:8b` model is pulled.

## Running the FastAPI / LangServe service
```bash
uvicorn api.app:app --reload
```
- Groq chat endpoint: `POST http://localhost:8000/groq/invoke`
- Essay endpoint (Ollama via prompt1): `POST http://localhost:8000/essay/invoke`
- Poem endpoint (Ollama via prompt2): `POST http://localhost:8000/poem/invoke`

## Streamlit demos
- API client UI (talks to the FastAPI service):
```bash
streamlit run api/client.py
```
- Groq celebrity Q&A demo:
```bash
streamlit run chatbot/main.py
```
- Local Ollama demo (requires Ollama running):
```bash
streamlit run chatbot/localllm.py
```

## LangGraph agent notebook
Open [agents/agents.ipynb](agents/agents.ipynb) and run cells top-to-bottom:
- Cell 1 installs packages.
- Cells 2-5 set up tools (Wikipedia, Arxiv, LangSmith retriever over LangSmith docs).
- Cell 6 configures the LLM (defaults to Groq; requires `GROQ_API_KEY`).
- Cell 7 builds the LangGraph ReAct agent.
- Cell 8 runs a sample question; adjust `recursion_limit` or the prompt as needed.
If using the LangSmith retriever, keep Ollama running so embeddings can be created.

## Git hygiene
The repo includes a [.gitignore](.gitignore) to exclude `.venv`, caches, and `.env`. Do not commit keys or the virtual environment.

## Pushing to GitHub (manual steps)
```bash
git status
# git init  # only if this isn't already a git repo
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/LangChain.git
git push -u origin main
```
Replace `<your-username>` with your GitHub handle. Ensure `.env` and `.venv/` stay untracked.
