import streamlit as st
import requests

# FastAPI endpoint URL
API_URL = "http://localhost:8000/query/"

def get_gemini_response(query):
    """Sends a query to the FastAPI endpoint and returns the response."""
    try:
        response = requests.post(API_URL, params={"query": query})
        response.raise_for_status() # add raise_for_status to catch error codes.
        # text = response.text.replace('\u00A0', ' ') 
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

st.title("Gemini API Query")

# Input Query
query = st.text_area("Enter your query:", height=150)

if st.button("Get Response"):
    if query:
        response = get_gemini_response(query)
        st.write("Response:")
        # st.write(response)
        st.markdown(response)
    else:
        st.warning("Please enter a query.")