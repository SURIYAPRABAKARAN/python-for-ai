from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# pdf load
pdf_path = "data/AI_Engineer_Roadmap.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()

# print(documents[0].page_content[:300])

# chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30
)

chunks = splitter.split_documents(documents)

# embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

# chroma db ( vector DB )
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

# retriving from chroma db we need top 3 mathcs so k = 3
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# ai model for response maker
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""
)