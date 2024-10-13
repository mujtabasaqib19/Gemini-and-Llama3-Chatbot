import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env
load_dotenv()

# Configure Google API key for Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up Llama3 model
llama_template = """ Answer the question.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Function to load the OpenAI Gemini model and get a response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Function to load the Llama3 model and get a response
def get_llama_response(context, question):
    model = OllamaLLM(model="llama3")
    prompt = ChatPromptTemplate.from_template(llama_template)
    chain = prompt | model
    result = chain.stream({"context": context, "question": question})
    return result

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini & Llama3 ChatBot Application")

# Model selection: Gemini or Llama3
model_choice = st.selectbox("Select Model", ["Gemini Pro", "Llama3"])

# Get user input
input_question = st.text_input("Input your question: ", key="input")

# Submit button
submit = st.button("Ask the question")

# Initialize conversation context if not present
if "context" not in st.session_state:
    st.session_state["context"] = ""

context = st.session_state["context"]

# If submit button is clicked
if submit:
    if model_choice == "Gemini Pro":
        # Gemini model response
        response = get_gemini_response(input_question)
        st.subheader("The Response from Gemini is:")
        for chunk in response:
            st.write(chunk.text)
            print("_" * 80)
        context += f"\nUser: {input_question}\nAI: {''.join(chunk.text for chunk in response)}"
    else:
        # Llama3 model response
        response = get_llama_response(context, input_question)
        st.subheader("The Response from Llama3 is:")
        st.write(response)
        context += f"\nUser: {input_question}\nAI: {response}"

    # Update conversation history in session state
    st.session_state["context"] = context
