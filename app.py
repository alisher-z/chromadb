# import chromadb
# from chromadb.utils import embedding_functions

# chrom_client = chromadb.Client()
# default_ef = embedding_functions.DefaultEmbeddingFunction()

# collection = chrom_client.get_or_create_collection('test_collection', embedding_function=default_ef)

# documents = [
#     {"id":"doc1", "text":"Hello, world!"},
#     {"id":"doc2", "text":"How are you today?"},
#     {"id":"doc3", "text":"Goodbye, see you later!"}
# ];

# ids = [doc['id'] for doc in documents]
# texts = [doc['text'] for doc in documents]

# collection.add(ids, documents=texts);

# results = collection.query(
#     query_texts='you',
#     n_results=3
# )

# print(results)

from database_orm import collection

documents = [
    {"id":"doc1", "text":"Hello, world!"},
    {"id":"doc2", "text":"How are you today?"},
    {"id":"doc3", "text":"Goodbye, see you later!"}
];

ids = [doc['id'] for doc in documents]
texts = [doc['text'] for doc in documents]

collection.add(ids, documents=texts);

query_txt = 'Age or the Earth'

result = collection.query(query_texts=query_txt, n_results=3)

print(result)

