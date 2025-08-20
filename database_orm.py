import chromadb
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()
db = chromadb.PersistentClient('./db/persisted')

collection = db.get_or_create_collection('info', embedding_function=default_ef)