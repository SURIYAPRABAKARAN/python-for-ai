# Load environment variables from .env file
from dotenv import load_dotenv

# PDF Loader
from langchain_community.document_loaders import PyPDFLoader

# Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Gemini Embedding Model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Vector Database
from langchain_chroma import Chroma

# Load GOOGLE_API_KEY
load_dotenv()


# ==================================================
# STEP 1 : LOAD PDF
# ==================================================

print("Loading PDF...")

loader = PyPDFLoader("data/AI_Engineer_Roadmap.pdf")

documents = loader.load()

print(f"Total Pages Loaded: {len(documents)}")


# ==================================================
# STEP 2 : SPLIT PDF INTO CHUNKS
# ==================================================

print("Creating Chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks Created: {len(chunks)}")


# ==================================================
# STEP 3 : LOAD EMBEDDING MODEL
# ==================================================

print("Loading Gemini Embedding Model...")

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)


# ==================================================
# STEP 4 : GENERATE EMBEDDINGS
# STEP 5 : STORE IN CHROMADB
# ==================================================

print("Creating ChromaDB and Storing Embeddings...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("✅ ChromaDB Created Successfully")
print("✅ Embeddings Stored Successfully")