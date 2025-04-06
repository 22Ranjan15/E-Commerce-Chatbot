from langchain_astradb import AstraDBVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
import os
import pandas as pd

from Components.data_convertion import dataConverter

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

embedding = GoogleGenerativeAIEmbeddings(api_key = GOOGLE_API_KEY, model = 'models/text-embedding-004')

def ingestData(status):
    vstore = AstraDBVectorStore(
        embedding = embedding,
        collection_name = "ecom_chatbot",
        api_endpoint = ASTRA_DB_API_ENDPOINT,
        token = ASTRA_DB_APPLICATION_TOKEN,
        namespace = ASTRA_DB_KEYSPACE,
    )
    
    storage = status
    if storage == None:
        docs = dataConverter()
        if docs is None:
            print("Warning: dataConverter() returned None.  No documents will be added.")
            inserted_ids = []  # Assign an empty list to inserted_ids
        else:
            inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, inserted_ids

if __name__=='__main__':
    vstore, inserted_ids = ingestData(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("Can you give me top 5 smartphone under 20000.")
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")
            