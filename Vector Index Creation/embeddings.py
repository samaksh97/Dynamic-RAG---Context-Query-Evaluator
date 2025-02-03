import numpy as np
from sentence_transformers import SentenceTransformer
class SentenceTransformerEmbeddingWrapper:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str):
        """
        Generates an embedding for a single text.

        Returns:
        np.array: A 1D array (embedding_dim,).
        """
        embedding = self.model.encode(text, convert_to_numpy=True)
        return embedding  # Ensure the embedding is 1D

    def embed_documents(self, texts: list):
        """
        Generates embeddings for a list of documents.

        Returns:
        np.array: A 2D array (num_documents, embedding_dim).
        """
        return np.array(self.model.encode(texts, convert_to_numpy=True))

    def embed_query(self, text: str):
        """
        Generates an embedding for a query.

        Returns:
        np.array: A 1D array (embedding_dim,).
        """
        return self.embed(text)

