# Multi-Pdf-Bot
This code is a Streamlit application that allows users to chat with multiple PDF documents. It utilizes various libraries and modules to process the PDFs, extract text from them, create a conversational AI model, and provide responses to user queries based on the content of the PDFs.

Let's go through the code step by step:

1. Importing Required Libraries:
   - `streamlit`: Used to create interactive web applications.
   - `dotenv`: Used to load environment variables.
   - `PdfReader` from `PyPDF2`: Used to read PDF documents.
   - Various modules from the `langchain` library: Used for text splitting, embeddings, vector stores, chat models, memory, chains, and LLMS (Language Learning Models).
   - `pandas`: Used for data manipulation and analysis.

2. Function Definitions:
   - `get_pdf_text(pdf_docs)`: Takes a list of PDF documents and extracts the text from them using `PdfReader`.
   - `get_text_chunks(text)`: Takes the extracted text as input and splits it into smaller chunks using a `CharacterTextSplitter` from the `langchain` library. This is done to enable efficient processing and retrieval of information.
   - `get_vectorstore(text_chunks)`: Takes the text chunks as input and creates a vector store using `OpenAIEmbeddings` from the `langchain` library.
   - `get_conversation_chain(vectorstore)`: Takes the vector store as input and creates a conversation chain using a chat model (`ChatOpenAI`) from the `langchain` library, along with a memory component (`ConversationBufferMemory`). This chain allows the system to engage in conversational interactions with the user based on the content of the PDFs.

3. `handle_userinput(user_question)`: Handles the user's input question. It sends the question to the conversation chain and retrieves the response. The conversation history is stored in the `st.session_state.chat_history` variable. The user's question and the chat history are displayed using HTML templates.

4. `main()`: The main function that serves as the entry point for the Streamlit application. It sets up the Streamlit page, handles user input, and processes the PDFs.
   - It first loads the environment variables and sets the page configuration.
   - It initializes the session state variables for conversation and chat history.
   - It creates a Streamlit sidebar where the user can upload multiple PDF documents.
   - When the user clicks the "Process" button, the PDFs are processed.
     - The PDFs' text is extracted using `get_pdf_text`.
     - The text is split into chunks using `get_text_chunks`.
     - A vector store is created using `get_vectorstore`.
     - A conversation chain is created using `get_conversation_chain`.
     - The chat history is cleared.
   - If a conversation chain exists, it checks if the chat history is empty. If so, it greets the user with a default message.
   - The user's question is input via a text input box, and the `handle_userinput` function is called to process the question.

5. The `if __name__ == '__main__':` block ensures that the `main()` function is executed when the script is run directly.

Overall, this code sets up a Streamlit application that allows users to upload multiple PDF documents, processes the documents to enable conversational interactions, and provides responses based on the content of the PDFs using a conversational AI model.

Run the Script:
`streamlit run app.py`
