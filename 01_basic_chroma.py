import chromadb
from docs import getDocs

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection('demonstration')

ids, texts = getDocs('basic')

print(ids)