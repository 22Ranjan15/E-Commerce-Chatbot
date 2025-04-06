import os
import logging
from flask import Flask, render_template, request
from dotenv import load_dotenv

# --- Import your custom components ---
# Make sure these paths are correct relative to app.py
# If Components is in the same directory as app.py:
from Components.retrieve_response import generateResponse
from Components.data_ingestion import ingestData
# If Components is structured differently, adjust the import path

# --- Configure logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Load Environment Variables ---
load_dotenv()
# Example: Ensure API keys needed by your components are in the .env file
# OPENAI_API_KEY=your_api_key_here

# --- Initialize Flask App ---
app = Flask(__name__) # Flask automatically looks for 'templates' and 'static' folders

# --- Initialize AI Components (Error Handling Recommended) ---
try:
    logging.info("Initializing data ingestion...")
    # Assuming ingestData returns the vector store object needed by generateResponse
    # Modify "done" if ingestData expects a path or other specific argument
    vstore = ingestData("done") # Or perhaps os.getenv("DATA_PATH")?
    logging.info("Data ingestion complete. Initializing response chain...")
    chain = generateResponse(vstore)
    logging.info("Response chain initialized.")
    AI_INITIALIZED = True
except Exception as e:
    logging.error(f"Failed to initialize AI components: {e}", exc_info=True)
    AI_INITIALIZED = False
    chain = None # Ensure chain is None if initialization fails


# --- Flask Routes ---
@app.route("/")
def index():
    """Serves the main chat page."""
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chat():
    """Handles incoming chat messages and returns AI response."""
    user_message = request.form.get("msg") # Use .get for safer access

    if not user_message:
        logging.warning("Received empty message.")
        return "Please type a message.", 400 # Bad request

    if not AI_INITIALIZED or not chain:
        logging.error("AI components not initialized. Cannot process request.")
        return "Sorry, the chatbot is currently unavailable due to an internal error.", 503 # Service unavailable

    try:
        logging.info(f"Received message: {user_message}")
        # --- Get AI response ---
        result = chain.invoke(user_message) # Pass the user message directly
        logging.info(f"Generated response: {result}")

        # Return the response as a plain string
        # Ensure 'result' is convertible to string. If it's a dict, extract the text.
        # Example if result is {'output_text': 'response'}: return str(result.get('output_text', ''))
        return str(result)

    except Exception as e:
        logging.error(f"Error processing message '{user_message}': {e}", exc_info=True)
        return "Sorry, I encountered an error trying to process your request.", 500 # Internal server error

# --- Run the App ---
if __name__ == '__main__':
    # Use environment variables for host and port if available, otherwise default
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "True").lower() == "true" # Debug mode from env var

    # Avoid running debug mode in production!
    if not debug_mode and os.getenv("FLASK_ENV") == "production":
         logging.warning("Running in production mode without debug enabled.")

    app.run(host=host, port=port, debug=debug_mode)