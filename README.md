# E-Commerce Chatbot for Mobile Devices

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
![Langchain](https://img.shields.io/badge/Langchain-%2316a75c.svg?style=flat&logo=data:image/svg%2Bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJMYW5nQ2hhaW4iIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Igp2aWV3Qm94PSIwIDAgNTAwIDUwMCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTAwIDUwMDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGcgaWQ9IkxheWVyXzEiPg0KPC9nPg0KPGcgaWQ9IkxheWVyXzIiPg0KPHBhdGggc3R5bGU9ImZpbGw6I2ZmZmYiIGQ9Ik0zNzMuNzYyLDE2OS42NjNjMCwwLTEyLjQxMS0yMi4wODItMzAuOTY4LTIyLjA4MmgtNzMuNzM0Yy0xOC41NTcsMC0zMS4wNjYsMjIuMDg2LTMxLjA2NiwyMi4wODZ2MTYwLjY3NWMwLDAsMTIuNTEsMjIuMDgyLDMxLjA2NiwyMi4wODJoNzMuNzM0YzE4LjU1NywwLDMwLjk2OC0yMi4wODIsMzAuOTY4LTIyLjA4MlYzMjkuNzQzYzAsMC0xMi40MTEtMjIuMDg2LTMwLjk2OC0yMi4wODZoLTczLjczNHYtMTYuNjY5aDczLjczNGMxOC41NTcsMCwzMC45NjgtMjIuMDg2LDMwLjk2OC0yMi4wODZWMjM2LjM0MWMwLDAsLTEyLjQxMS0yMi4wODItMzAuOTY4LTIyLjA4MnoiLz4NCjxwYXRoIHN0eWxlPSJmaWxsOiNGRjY0MDA7IiBkPSJNMjYwLjQzNywxNjkuNjYzYzAsMC0xMi40MTEtMjIuMDg2LTMxLjA2Ni0yMi4wODZoLTczLjczNGMtMTguNTU3LDAtMzAuOTY4LDIyLjA4Mi0zMC45NjgsMjIuMDgydiAxNjAuNjc1YzAsMCwxMi41MSwyMi4wODIsMzEuMDY2LDIyLjA4Mmg3My43MzRjMTguNTU3LDAsMzAuOTY4LTIyLjA4MiwzMC45NjgtMjIuMDg2VjMyOS43NDNjMCwwLTEyLjQxMS0yMi4wODItMzAuOTY4LTIyLjA4MmgtNzMuNzM0di0xNi42NjloNzMuNzM0YzE4LjU1NywwLDMwLjk2OC0yMi4wODIsMzAuOTY4LTIyLjA4NlYyMzYuMzQxYzAsMC0xMi40MTEtMjIuMDg2LTMxLjA2Ni0yMi4wODZIMTg2LjcwM3YxNjAuNjc1aC0xNi42NjljMCwwLTEyLjQxMS0yMi4wODItMzAuOTY4LTIyLjA4MmgtNzMuNzM0YzE4LjU1NywwLDMwLjk2OCwyMi4wODIsMzAuOTY4LDIyLjA4MlYzMjkuNzQzYzAsMC0xMi40MTEtMjIuMDg2LTMwLjk2OC0yMi4wODJoLTczLjczNHYtMTYuNjY5aDczLjczNGMxOC41NTcsMCwzMC45NjgtMjIuMDg2LDMwLjk2OC0yMi4wODZWMjM2LjM0MWMwLDAsLTEyLjQxMS0yMi4wODItMzAuOTY4LTIyLjA4MnoiLz4NCjwvZz4NCjwvc3ZnPg0K)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat&logo=google-gemini)
![Astra DB](https://img.shields.io/badge/Astra%20DB-00ADD8?style=flat&logo=astra)
![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=flat&logo=flask&logoColor=white)

## Overview

This project implements an e-commerce chatbot specializing in mobile devices. It leverages the power of Large Language Models (LLMs) through `Langchain`, utilizes `Google Gemini` for text embedding and response generation, and employs `Astra DB` as a vector store for efficient retrieval of product information. The chatbot is designed to understand user queries related to smartphones, search through a dataset of mobile specifications, and provide relevant recommendations and information.

The application consists of the following key components:

- **Data Ingestion and Conversion:** Reads a CSV dataset of mobile phone specifications, transforms it into Langchain `Document` objects, and stores the embeddings in Astra DB.
- **Vector Store:** Uses Astra DB to store and efficiently query vector embeddings of the product data, enabling semantic search capabilities.
- **Language Model Integration:** Employs Google Gemini's embedding model to create vector representations of the product data and its generative model to formulate responses based on retrieved information.
- **Chat Interface:** A user-friendly web interface built with Flask, allowing users to interact with the chatbot through text messages.

## Features

- **Intelligent Product Search:** Understands natural language queries to find relevant mobile phones based on specifications like price, features, and brand.
- **Context-Aware Responses:** Generates informative and concise answers by leveraging the context from the product dataset.
- **Scalable Data Storage:** Utilizes Astra DB, a cloud-native vector database, for scalable and efficient storage and retrieval of product information.
- **User-Friendly Interface:** Provides a simple and intuitive web interface for seamless interaction.
- **Error Handling:** Implements robust error handling for data loading, AI component initialization, and message processing.

## Technologies Used

- **Python 3.10**
- **Langchain**
- **Langchain AstraDB** 
- **Langchain Google GenAI** 
- **Google Generative AI (Gemini)**
- **Astra DB**
- **Flask**
- **Pandas**
- **python-dotenv**

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/22Ranjan15/E-Commerce-Chatbot.git
    ```
2. **Install Demendencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Set up Environment Variables:**
    - Create a `.env` file in the root directory of the project. 
    - Add the following environment variables, replacing the placeholders with your actual API keys and Astra DB credentials:

    ```bash
    GOOGLE_API_KEY = YOUR_GOOGLE_GEMINI_API_KEY
    ASTRA_DB_API_ENDPOINT = YOUR_ASTRA_DB_API_ENDPOINT
    ASTRA_DB_APPLICATION_TOKEN = YOUR_ASTRA_DB_APPLICATION_TOKEN
    ASTRA_DB_KEYSPACE = YOUR_ASTRA_DB_KEYSPACE_NAME
    ```
    - Ensure you have an Astra DB database and a vector collection named `ecom_chatbot` created in the specified keyspace.

4. **Run the Flask Application:**
    ```bash
    python app.py
    ```
6. **Access the Chatbot:**
    - Open your web browser and navigate to `http://127.0.0.1:5000/` (or the host and port you configured in the `.env` file).


## Project Structure
```
.
├── .env
├── .gitignore
├── README.md
├── LISENSE
├── setup.py
├── requirements.txt
├── Data/
│   ├── Mobiles Dataset (2025).csv
│   └── .gitkeep
├── Demo/
│   └── .gitkeep
├── Notebooks/
│   └── experiments.ipynb
├── Components/
│   ├── __init__.py
│   ├── data_convertion.py
│   ├── data_ingestion.py
│   └── retrieve_response.py
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── app.py
```
## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.   

## Acknowledgements

* Built using the powerful [Flask](https://flask.palletsprojects.com/) framework.
* Leverages the flexible [LangChain](https://www.langchain.com) library for LLM orchestration.
* Powered by [Google Gemini](https://deepmind.google/technologies/gemini/).
* Utilizes [Astra DB](https://astra.datastax.com/), a scalable vector database, for efficient storage and retrieval.
