import os
import streamlit as st
from doc_chat_utility import get_answer

working_directory = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="DocAnalyzer",
    page_icon="📝",
    layout="centered"
)

st.title("📄🔎 Document Analyzer")
st.write("Built using Meta's Llama 3 🦙, this app provides precise and insightful answers to your queries.")
st.write("Note: Initial processing may take a bit of time as the app sets up the intelligent backend to deliver accurate responses.")
st.write("")

uploaded_file = st.file_uploader(label="Upload your file", type=['pdf'])

user_query = st.text_input(label="", placeholder="Ask your question...")

if st.button("Run"):
    bytes_data = uploaded_file.read()
    file_name = uploaded_file.name
    # save the file to the working directory
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, "wb") as f:
        f.write(bytes_data)
    answer = get_answer(file_name, user_query)

    st.success(answer)
