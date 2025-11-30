---
id: 001
title: RAG Chat Backend RPS Benchmarks
stage: misc
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 002-physical-ai-course
user: Kashan
command: Investigate typical Requests Per Second (RPS) benchmarks or reasonable performance expectations for a FastAPI backend handling RAG (Retrieval Augmented Generation) chat requests. Consider factors like vector database interaction (Qdrant), LLM calls (OpenAI API), and user authentication (Better-Auth). Provide a reasonable target RPS for a new project of this nature. Output the findings in markdown format, suitable for inclusion in `research.md`.
labels: ["performance","benchmarks","fastapi","rag","qdrant","openai"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- C:\Users\Kashan\Documents\claude code\Robotics\research.md
tests:
null
---

## Prompt

Investigate typical Requests Per Second (RPS) benchmarks or reasonable performance expectations for a FastAPI backend handling RAG (Retrieval Augmented Generation) chat requests. Consider factors like vector database interaction (Qdrant), LLM calls (OpenAI API), and user authentication (Better-Auth). Provide a reasonable target RPS for a new project of this nature. Output the findings in markdown format, suitable for inclusion in `research.md`.

## Response snapshot

This document outlines reasonable performance expectations and a target Requests Per Second (RPS) for a new FastAPI backend handling Retrieval Augmented Generation (RAG) chat requests, considering key components such as Qdrant for vector database interaction, OpenAI API for Large Language Model (LLM) calls, and user authentication.

### Component Performance Considerations:

1.  **FastAPI:**
    FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. Its asynchronous capabilities allow it to handle a high volume of concurrent requests efficiently, making it well-suited for RAG APIs.

2.  **Qdrant (Vector Database):**
    Qdrant is designed for high-dimensional vector storage and efficient similarity search. Benchmarks indicate its strong performance in RAG systems, even with multi-million-vector datasets. Internal benchmarking suggests similarity search times of less than 100 milliseconds and the ability to handle over 1,000 concurrent API requests with consistent throughput. This demonstrates Qdrant's capability to be a high-throughput component within the RAG architecture.

3.  **OpenAI API (LLM Calls):**
    The OpenAI API is crucial for two main aspects of RAG: creating vector embeddings of documents and generating human-like responses. The performance of the OpenAI API (latency and rate limits) will be a significant factor in the overall end-to-end latency of a RAG chat request. While the API itself is highly optimized, the time taken for a full LLM inference can vary and directly impact the achievable RPS.

4.  **User Authentication (Better-Auth):**
    While "Better-Auth" was mentioned as a component, specific performance benchmarks or detailed information regarding its impact on RPS within a FastAPI RAG context were not found in the initial search. Generally, authentication and authorization mechanisms introduce some overhead. However, for most well-implemented authentication systems, this overhead is typically a small fraction of the total request time compared to vector database lookups and LLM inference, especially for simple token-based or session-based authentication. Optimizing authentication performance is generally a secondary concern to LLM and vector store performance in RAG systems, unless dealing with extremely high authentication loads or complex authorization policies.

### Target RPS for a New Project:

Given the high-performance nature of FastAPI and Qdrant, the primary bottleneck for RPS in a RAG chat system is most likely to be the latency associated with the OpenAI API calls. A single RAG chat request involves:

1.  User input processing.
2.  Vector search in Qdrant.
3.  Context retrieval.
4.  OpenAI API call for generation.
5.  Response processing.

Considering Qdrant's ability to handle over 1,000 concurrent requests and FastAPI's efficiency, a reasonable initial target RPS for a *new* RAG chat project, assuming average LLM response times (which can range from a few hundred milliseconds to several seconds depending on model complexity and response length), would be in the range of **5-20 RPS per instance**.

This range is a conservative starting point. With optimization techniques, caching, efficient prompt engineering, careful selection of LLM models, and potentially batching LLM calls, higher RPS can be achieved. For example, if the average end-to-end request time (dominated by LLM inference) is 500ms (0.5 seconds), a single threaded process could theoretically handle 2 RPS. With asynchronous processing, multiple workers, and efficient I/O, this number can scale significantly.

### Recommendations for Achieving Target RPS:

*   **Asynchronous Processing:** Leverage FastAPI's `async/await` capabilities for all I/O-bound operations (Qdrant calls, OpenAI API calls).
*   **Load Balancing and Horizontal Scaling:** Deploy multiple instances of the FastAPI application behind a load balancer to distribute traffic.
*   **Caching:** Implement caching for frequently accessed RAG contexts or even entire generated responses where appropriate.
*   **LLM Optimization:**
    *   Choose appropriate LLM models based on latency and cost requirements.
    *   Optimize prompt lengths and complexity.
    *   Consider streaming LLM responses if applicable.
*   **Qdrant Optimization:** Ensure Qdrant is well-indexed and running on adequately provisioned hardware.
*   **Monitoring and Profiling:** Continuously monitor the application's performance and profile bottlenecks to identify areas for improvement.

## Outcome

- ✅ Impact: Provided a comprehensive overview of RAG component performance and a reasonable target RPS.
- 🧪 Tests: No tests were run.
- 📁 Files: One new file created: research.md
- 🔁 Next prompts: Awaiting user's next request.
- 🧠 Reflection: Successfully gathered and synthesized information from web search to answer the user's query.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
