# Load environment variables
from dotenv import load_dotenv

# Gemini Embedding Model
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Gemini Chat Model
from langchain_google_genai import ChatGoogleGenerativeAI

# ChromaDB
from langchain_chroma import Chroma

# Prompt Template
from langchain_core.prompts import PromptTemplate

# LCEL Components
from langchain_core.runnables import RunnablePassthrough

# Output Parser
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# ==================================================
# STEP 1 : LOAD EMBEDDING MODEL
# ==================================================

print("Loading Embedding Model...")

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)


# ==================================================
# STEP 2 : LOAD EXISTING CHROMADB
# ==================================================

print("Loading ChromaDB...")

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


# ==================================================
# STEP 3 : CREATE RETRIEVER
# TOP 3 MATCHING CHUNKS
# ==================================================

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

print("Retriever Ready")


# ==================================================
# STEP 4 : LOAD GEMINI CHAT MODEL
# ==================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

print("Gemini Model Loaded")


# ==================================================
# STEP 5 : CREATE PROMPT TEMPLATE
# ==================================================

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


# ==================================================
# STEP 6 : CREATE RETRIEVAL CHAIN (LCEL)
# ==================================================

chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

print("LCEL Retrieval Chain Ready")


# ==================================================
# STEP 7 : CHAT LOOP
# ==================================================

while True:

    question = input("\nAsk Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    print("\nSearching ChromaDB...")

    response = chain.invoke(question)

    print("\nAnswer:")
    print(response)