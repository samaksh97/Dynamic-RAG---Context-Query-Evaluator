PGVECTOR_CONNECTION_STRING='' 
COLLECTION_NAME = "current_affairs_1" # check and add the collection you need
SIMILARITY_THRESHOLD = 0.01 #Threshold reduced for GUSE
K = 3

USERNAME = 'samaksh_gulati'
PASSWORD = 'Kshitij1993@'


FIRST_PROMPT = """[INST] 
You are a knowledgeable assistant specialized in answering general knowledge questions.

Context:
{s}

Question:
{question}


Instructions:
1. Only use the retrieved context to answer the question. Do not use any internal or private knowledge.
2. If the answer is not in the retrieved context, respond with: "I do not know that, but I can help you look it up."


"""
