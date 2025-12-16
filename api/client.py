# import requests 
# import streamlit as st

# def get_groq_response(input_text):
#     response = requests.post("http://localhost:8000/groq/invoke", 
#     json={'input': {'topic': input_text}})
#     return response.json()['output']

# def get_ollama_response(input_text):
#     response = requests.post("http://localhost:8000/poem/invoke", 
#     json={'input': {'topic': input_text}})
#     return response.json()['output']


# st.title("LangChain API Client Demo")
# input_text = st.text_input("Enter a essay topic")
# input_text1 = st.text_input("Enter a poem topic ")

# if input_text:
#     with st.spinner("Generating essay..."):
#         essay = get_groq_response(input_text)
#         st.subheader("Generated Essay:")
#         st.write(essay)

# if input_text1:
#     with st.spinner("Generating poem..."):
#         poem = get_ollama_response(input_text1)
#         st.subheader("Generated Poem:")
#         st.write(poem)


import requests
import streamlit as st

def get_groq_response(input_text):
    # response = requests.post(
    #     "http://localhost:8000/essay/invoke",
    #     json={'input': {'topic': input_text}}
    # )

    # st.write("Status code:", response.status_code)
    # st.write("Raw response:", response.text)

    # return response.json()['output']
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={'input': {'topic': input_text}}
        )
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        # If the request was successful, parse the JSON and return the output
        return response.json()['output']
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        return f"Error connecting to server: {e}"
    except KeyError:
        # Handle cases where the JSON response doesn't have the 'output' key
        return "Error: Received an unexpected response format from the server."
    except requests.exceptions.JSONDecodeError:
        # Handle cases where the response is not valid JSON
        return f"Error: Failed to decode server response. Status: {response.status_code}, Body: {response.text}"

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_groq_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))