import os
import openai
import time
from dotenv import load_dotenv, find_dotenv
from llama_index import VectorStoreIndex, SimpleDirectoryReader

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]


def ask_doc(question):
    # Start the timer
    start_time = time.time()
    
    # Query the document
    documents = SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(question).response

    # End the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Print the response and elapsed time
    # print(f"Response: {response}")
    # print(f"Elapsed time: {elapsed_time} seconds")
    
    return response