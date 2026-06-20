# from pdf_loader import load_pdf
# from chunker import create_chunks
# from embedding_test import load_dotenv
# from chroma_service import store_chunks , get_chunk_count , search_chunks

# pdf_path = "data/AI_Engineer_Roadmap.pdf"

# # pdf readed and converted to words
# pdf_to_words = load_pdf(pdf_path)

# # words spilted into small size of chunks wiht list obj
# chunks = create_chunks(pdf_to_words)

# # print(f"chunks : {chunks}")

# # print(f"chunks len: {len(chunks)}")

# # now chunks into embadings words to vector format.
# store_chunks(chunks)

# count_of_embdings_inVector_db = get_chunk_count()

# # print(f"count_of_embdings_inVector_db : {count_of_embdings_inVector_db}")

# data_from_chroma_Db = search_chunks("Functions and recursion is there in side db ?")

# print(f"data_from_chroma_Db : {data_from_chroma_Db}")

from rag_service import ask_question

question = input("Ask Question: ")

answer = ask_question(question)

print("\nAnswer:\n")
print(answer)