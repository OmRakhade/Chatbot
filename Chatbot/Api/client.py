import requests
import streamlit as st
import json

# Function to get model response from /manual_query endpoint
def get_model_response_manual_query(input_text, language):
    url = "http://localhost:8000/manual_query"  # Changed endpoint to /manual_query
    headers = {'Content-Type': 'application/json'} # Explicitly set content type to json
    payload = json.dumps({ # Use json.dumps to serialize payload to JSON string
        "query": input_text,
        "language": language # Include language in the payload
    })
    try:
        response = requests.post(url, headers=headers, data=payload) # Send data as JSON
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()['result'] # Access 'result' key as defined in manual_query endpoint
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    except KeyError:
        return "Error: Unexpected response format from the API. Missing 'result' key."
    except json.JSONDecodeError: # Handle potential JSON decode error
        return "Error: Could not decode JSON response from API."

st.title('Chatbot with LLAMA2 API')

language_choice = st.radio(
    "Choose Output Language:",
    ("en", "mr", "hi"),  # Language codes
    index=0,  # Default to English
    format_func=lambda x: {"en": "English", "mr": "Marathi", "hi": "Hindi"}[x] # Display names
)

input_text = st.text_area("Write a query to solve your doubts?")

if input_text:
    st.subheader("Response in " + {"en": "English", "mr": "Marathi", "hi": "Hindi"}[language_choice] + ":") # Display chosen language
    response_output = get_model_response_manual_query(input_text, language_choice) # Pass language choice to function
    st.write(response_output)