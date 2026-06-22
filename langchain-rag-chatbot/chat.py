from ingest import retriever, llm, prompt

question = input("Ask: ")

docs = retriever.invoke(question)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

final_prompt = prompt.format(
    context=context,
    question=question
)

response = llm.invoke(final_prompt)

print(response.content)