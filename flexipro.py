import streamlit as st
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from serpapi import GoogleSearch
import os 
from dotenv import load_dotenv
load_dotenv("C:\\Users\\vamsi\\project\\key.env")

# Set API Keys
API_KEY = os.getenv("openAI_API_key")
serpapi_key = os.getenv("serpapi_key")

# Initialize LLM
llm = OpenAI(temperature=0.7, api_key=API_KEY)

# Function to fetch data from SerpAPI
def fetch_intellinum_data():
    try:
        search = GoogleSearch({"q": "Intellinum company details", "api_key": serpapi_key})
        results = search.get_dict()

        # Extract relevant data from the results
        company_info = []
        for result in results.get("organic_results", []):
            title = result.get("title", "No Title")
            snippet = result.get("snippet", "No Snippet")
            company_info.append(f"{title}: {snippet}")
        
        return "\n".join(company_info) if company_info else "No relevant data found."
    except Exception as e:
        return f"Error fetching data from SerpAPI: {str(e)}"

# Define Chatbot Logic
def generate_response(topic):
    # Fetch data from SerpAPI
    web_data = fetch_intellinum_data()

    # OpenAI Prompt
    prompt_template = PromptTemplate(
        input_variables=["topic", "web_info"],
        template=(
            "You are a supply chain expert. Answer queries about {topic} based on the following real-world data:\n\n"
            "{web_info}\n\n"
            "Provide a detailed response that combines general knowledge with the given data."
        ),
    )

    # Generate Response
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run({"topic": topic, "web_info": web_data})
    return response

# Streamlit UI
st.title("Supply Chain Chatbot")
query = st.text_input("Enter your query about FlexiPro or Intellinum:")

if query:
    response = generate_response(query)
    st.write("**Chatbot Response:**")
    st.write(response)
