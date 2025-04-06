from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from Components.data_ingestion import ingestData


def generateResponse(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
        You are an e-commerce bot specializing in product recommendations and customer support. 
        You analyze product details to provide accurate, helpful, and relevant responses.
        Focus on answering the question using the provided context, and keep your answers concise and informative.
        Avoid making up information or straying from the product context.

        CONTEXT:
        {context}

        QUESTION: {question}

        YOUR ANSWER:
    """

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    llm = ChatGoogleGenerativeAI(model='models/gemini-2.0-flash')

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__=='__main__':
    vstore = ingestData("done")
    chain  = generateResponse(vstore)
    print(chain.invoke("Can you tell me the best smartphone under 30000?"))
    
    
    
    