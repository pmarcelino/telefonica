import main
import openai
import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from streamlit_chat import message

# Set page title and header
st.set_page_config(page_title="Telefónica", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Análise de documento</h1>", unsafe_allow_html=True)

# Set API key
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]


# Start session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Sidebar
st.sidebar.title("Ações")
clear_button = st.sidebar.button("Limpar conversa", key="clear")

# Reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    response = main.ask_doc(prompt)
    print("response: ", response)
    
    st.session_state['messages'].append({"role": "assistant", "content": response})

    return response


# Container for chat history
response_container = st.container()
# Container for text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Thaís 👸:", key='input', height=100)
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button and user_input:
        output = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))