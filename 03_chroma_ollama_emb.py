import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from docs import getDocs

chroma_client = chromadb.PersistentClient('./db/persisted')
ollam_ef = OllamaEmbeddingFunction(url='http://localhost:11434', model_name='nomic-embed-text')

collection = chroma_client.get_or_create_collection('ollama-ef', embedding_function=ollam_ef)

ids, texts = getDocs('advanced')

collection.add(ids, documents=texts)

query_text = 'find document related to turing test'

result = collection.query(query_texts=query_text, n_results=3)

print(result)