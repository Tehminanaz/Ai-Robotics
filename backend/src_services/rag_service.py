from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from src.services.qdrant_service import retrieve_chunks
from typing import List

async def run_rag_query(query_text: str) -> str:
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # In a full LangChain setup, you would have a Retriever.
    # For this task, we'll directly call retrieve_chunks and format the context.
    retrieved_docs = await retrieve_chunks(query_text)
    context = "\n\n".join([doc.text_snippet for doc in retrieved_docs])

    if not context:
        return "I'm sorry, I couldn't find any relevant information to answer your query."

    prompt_template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

    Question: {question}
    """
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = PROMPT | llm

    response = await chain.ainvoke({"context": context, "question": query_text})
    return response.content
