import chromadb
from docs import getDocs

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection('demonstration')

ids, texts = getDocs('basic')

collection.add(ids, documents=texts)

query_text = 'Hello, world!'

result = collection.query(query_texts=query_text, n_results=3)

print(result)