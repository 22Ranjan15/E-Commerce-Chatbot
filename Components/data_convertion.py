import pandas as pd
from langchain_core.documents import Document

def dataConverter():
    try:
        # Loading Dataset
        data_path = "E:\Data Science\Projects\Custom E-Commerce Chatbot\Data\Mobiles Dataset (2025).csv"
        try:
            data = pd.read_csv(data_path, encoding='latin-1') 
        except UnicodeDecodeError:
            try:
                data = pd.read_csv(data_path, encoding='cp1252')
            except UnicodeDecodeError:
                data = pd.read_csv(data_path, encoding='utf-8')  

        # Selecting Necessary Data Columns
        data = data[
            [
                'Company Name', 'Model Name', 'Mobile Weight', 'RAM', 
                'Front Camera', 'Back Camera', 'Processor', 'Battery Capacity', 
                'Screen Size', 'Launched Price (India)', 'Launched Year'
            ]
        ]

        # Converting the Dataset into JSON format
        product_list = []
        for index, row in data.iterrows():
            obj = {
                'company': row['Company Name'],
                'model': row['Model Name'],
                'mobile_weight': row['Mobile Weight'],
                'ram': row['RAM'],
                'front_camera': row['Front Camera'],
                'back_camera': row['Back Camera'],
                'processor': row['Processor'],
                'battery': row['Battery Capacity'],
                'screen_size': row['Screen Size'],
                'price': row['Launched Price (India)'],
                'launched_year': row['Launched Year']
            }
            product_list.append(obj)

        # Converting this JSON data into langchain document 
        docs = []
        for entry in product_list:
            metadata = {
                'company': entry['company'],
                'model': entry['model'],
                'price': entry['price'],
                'launched_year': entry['launched_year']
            }
            content = f"Company: {entry['company']}, Model: {entry['model']}, Weight: {entry['mobile_weight']}, RAM: {entry['ram']}, Front Camera: {entry['front_camera']}, Back Camera: {entry['back_camera']}, Processor: {entry['processor']}, Battery: {entry['battery']}, Screen Size: {entry['screen_size']}, Price: {entry['price']}, Launched Year: {entry['launched_year']}"
            doc = Document(page_content=content, metadata=metadata)
            docs.append(doc)

        return docs  # Return the list of documents

    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list in case of an error



if __name__ == '__main__':
    documents = dataConverter()
    if documents:
        print(f"Number of documents created: {len(documents)}")
        # Print the content of the first document as a sample
        print("\nSample Document:")
        print(f"Content: {documents[0].page_content}")
        print(f"Metadata: {documents[0].metadata}")
    else:
        print("No documents were created.")