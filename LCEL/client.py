import requests
import streamlit as st
from streamlit_chat import message


def get_groq_response(input_text):
    json_body = {
        "input": {
            "language": "bangla",
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    # Use 'json' to send JSON payload
    response = requests.post(
        "http://127.0.0.1:8000/translate/invoke", 
        json=json_body
    )
    
    # Ensure the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API call failed with status code {response.status_code}", "detail": response.text}

## Streamlit app
st.title(" বদলাও ১.০ : নিজের ভাষায় শেখ সবকিছু !")
input_text = st.text_input("Enter the text you want to convert to Bangla")

if input_text:
    result = get_groq_response(input_text)
    #st.write(result)
    st.write(message(result["output"]))
   