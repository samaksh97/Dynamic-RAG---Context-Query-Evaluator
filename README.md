# Dynamic RAG Query System with LangChain and PostgreSQL

## Overview
This repository provides a framework for a **Retrieval-Augmented Generation (RAG) system** using **LangChain**, **PostgreSQL with PGVector**, and an **LLM** to dynamically process and answer queries. It includes modules for:
- Initializing a **vector store** for efficient retrieval.
- Implementing a **Conversational Retrieval Chain** for adaptive query responses.
- Evaluating context quality through **semantic similarity** and **keyword matching**.
- Performing **fact-checking** on retrieved documents.
- Generating **summaries** using **Azure OpenAI**.

## Prerequisites
Before using this system, ensure you have:
- **Python 3.8+** installed.
- **PostgreSQL** with **PGVector** extension set up.
- **API access** to an LLM (e.g., Azure OpenAI).
- **Fact-checking API key** (optional, but required for claim validation).
- **Proxy settings** configured (if required by your network).

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo.git
cd your-repo
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory with the following contents:
```sh
USERNAME=your_proxy_username
PASSWORD=your_proxy_password
PGVECTOR_CONNECTION_STRING=your_pgvector_connection_string
COLLECTION_NAME=your_collection_name
```

If a proxy is required, the script automatically configures:
```sh
os.environ["HTTP_PROXY"] = f"http://{USERNAME}:{PASSWORD}@proxy.ins.dell.com:80"
```

## Features

### 1. Initialize Vector Store
The `initialize_vector_store` function sets up a **PGVector** store using **SentenceTransformers** for embedding storage and retrieval.

### 2. Conversational Retrieval Chain
The `create_dynamic_rag_chain` function dynamically selects the number of documents (`k`) to retrieve based on query needs, optimizing recall while maintaining relevance.

### 3. Fact-Checking Functionality
The `fact_check_dataframe` function uses an external API to validate claims against context data stored in a **DataFrame**.

### 4. Context Evaluation
The `evaluate_final_context` function computes the quality of retrieved documents using:
- **Semantic Similarity**
- **Keyword Matching**
- **Context Length Penalty**
- **Optional Fact-Checking Score**

### 5. Generating Summaries with LLM
The `generate_summary_with_llm` function produces a user-friendly explanation of retrieved documents and evaluation metrics.

### 6. Query Handling Pipeline
The `answer_query_with_dynamic_rag` function dynamically selects the optimal number of retrieved chunks, evaluates them, and refines responses using:
- **Initial RAG retrieval**
- **Semantic and keyword scoring**
- **Selection of optimal context size**
- **Final response generation**

## Usage

To handle queries dynamically:
```python
from main import answer_query_with_dynamic_rag

response = answer_query_with_dynamic_rag(
    query="What is the latest update on AI models?",
    chat_history=[],
    store=initialize_vector_store(),
    azure_llm=LangchainDSXLLM(),
    prompt=PromptTemplate(...),
    text_processor=TextProcessor(),
    semantic_similarity=SemanticSimilarity(),
    api_key="your_fact_checking_api_key"
)

print(response["answer"])
```

## Notes
- Ensure **PostgreSQL** is running and the **PGVector** collection is set up before executing queries.
- If using a **corporate proxy**, configure the `.env` file accordingly.
- **Fact-checking** requires an API key from **Bespoke Labs**.

## License
This project is licensed under the **MIT License**.

## Contributors
- **Samaksh Gulati**
- **Jasleen Singh**

