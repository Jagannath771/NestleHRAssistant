# Import necessary libraries
import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
import gradio as gr

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key for language model interactions
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Load the PDF document
# Use PyPDFLoader to load and process the PDF file
loader = PyPDFLoader("humanresourcespolicy.pdf")
documents = loader.load()  # This will extract the text from the PDF

# Split the document into manageable chunks for processing
# CharacterTextSplitter helps in breaking down large texts for embedding
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)  # This creates smaller, 1000-character chunks


# Generate embeddings (vector representations) for the chunks of text
# Using OpenAI embeddings to convert text into numerical form that can be searched efficiently
embeddings = OpenAIEmbeddings()

# Create a vector database using Chroma to store the document chunks and their embeddings
# This allows fast retrieval of relevant text chunks during Q&A
docsearch = Chroma.from_documents(texts, embeddings)

# Create a question-answering chain using the stored document vectors
# The chain_type 'stuff' combines retrieved chunks into a coherent response
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),  # Language model used for generating responses
    chain_type="stuff",  # Chain type that retrieves and combines relevant chunks
    retriever=docsearch.as_retriever()  # Retriever for the vector store
)

# Define the Gradio interface for the chatbot
# Gradio simplifies creating web interfaces for AI applications
def chatbot(query):
    # Pass the user's query to the QA system and return the response
    response = qa.invoke(query)
    return response['result'].strip('/n')

# Setting up a professional and user-friendly interface
iface = gr.Interface(
    fn=chatbot,  # The chatbot function that handles the query and returns an answer
    inputs=gr.Textbox(lines=2, placeholder="Ask about HR policies..."),  # Input box for user queries
    outputs="text",  # The output will be displayed as plain text
    title="Nestle HR Policy Assistant",  # Professional title for the web interface
    description="Ask questions about Nestle's Human Resource policies. This tool will provide quick answers based on the company's HR policy document.",  # Descriptive text for users
    theme="dark",  # A dark theme for a professional, modern look
    examples=[  # Add some example questions for user guidance
        "What is the policy on employee vacation days?",
        "How are promotions handled in Nestle?",
        "What are the benefits provided to employees?"
    ]
)

# Launch the Gradio interface for users to interact with the chatbot
# Gradio will automatically launch a browser window with the interface
iface.launch(share=True)
