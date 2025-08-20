import chromadb
from chromadb.utils import embedding_functions
from docs import getDocs

chroma_client = chromadb.PersistentClient('./db/persisted')
default_ef = embedding_functions.DefaultEmbeddingFunction()
collection = chroma_client.get_or_create_collection('demonstration', embedding_function=default_ef)

ids, texts = getDocs('intermediate')

collection.add(ids, documents=texts)

query_texts = 'Age of Earth'

result = collection.query(query_texts=query_texts, n_results=3)

print(result)