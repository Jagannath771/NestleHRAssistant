🏢 HR Policy Assistant
A question-answering chatbot built using LangChain, OpenAI, and Gradio, designed to help users query Human Resources policy documents. The chatbot utilizes a PDF document of HR policies, processes it, and allows users to ask questions in natural language to get accurate answers.
Link for the Project :- https://huggingface.co/spaces/Jagannath771/Nestle-HR

📖 Project Overview
The HR Policy Assistant is a document-based chatbot that retrieves answers from a company's HR policy document. It uses LangChain to load, split, and vectorize the document, and then serves as a question-answering system by leveraging OpenAI's GPT models. The web interface is built using Gradio, offering an interactive and user-friendly environment to query HR policies efficiently.

Key Features:
📄 PDF Document Processing: Automatically loads and splits the HR policy document for easy access and retrieval.
🤖 OpenAI's GPT: Uses state-of-the-art language models to generate precise and relevant responses.
⚡ Fast Retrieval: Answers are fetched quickly using vectorized text search with Chroma.
🌐 Interactive Interface: Built with Gradio for easy user interaction.
🚀 Live Demo
You can launch the project locally by following the setup instructions below.

🛠️ Installation and Setup
Prerequisites
Before you begin, ensure you have the following tools installed:

Python 3.8+
OpenAI API Key
pip
Step-by-Step Guide
Clone the repository:

bash
Copy code
git clone https://github.com/Jagannath771/NestleHRAssistant.git
cd hr-policy-assistant
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory of the project.
Add your OpenAI API key:
bash
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Add the HR policy document:

Place the HR policy PDF you want to use in the root directory of the project. Make sure the file is named humanresourcespolicy.pdf or adjust the code accordingly.
Run the application:

bash
Copy code
python app.py
Gradio will launch a local server, and you will be able to interact with the chatbot in your browser.

🖥️ Usage
Start the app and wait for the Gradio interface to load in your web browser.
Ask any questions related to HR policies by typing into the textbox (e.g., "What is the leave policy for employees?" or "How are promotions handled?").
The chatbot will provide precise answers based on the loaded HR document.
Example Queries:
"What is the policy on employee vacation days?"
"How does the company handle promotions?"
"What benefits do employees get?"
🧰 Technologies Used
LangChain: For document loading, splitting, and vector search.
OpenAI: GPT language models to generate answers.
Chroma: For efficient document storage and retrieval.
Gradio: For building an easy-to-use web interface.
PyPDFLoader: For PDF document parsing.
📁 Project Structure
bash
Copy code
Nestle-HR-Assistant/
│
├── app.py                   # Main application script
├── humanresourcespolicy.pdf  # HR policy document (PDF)
├── requirements.txt          # List of dependencies
├── .env                      # Environment variables (API key)
├── README.md                 # Project documentation (this file)
└── .gitignore                # Files to ignore in the repository

Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a Pull Request.
