import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="pdf_chunks"
)

def store_chunks(chunks):

    for index, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            ids=[str(index)]
        )

def get_chunk_count():

    return collection.count()

def search_chunks(query, n_results=3):

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results