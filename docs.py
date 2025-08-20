basic_docs = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"}
]

intermediate_docs = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {
        "id": "doc4",
        "text": "Microsoft is a technology company that develops software. It was founded by Bill Gates and Paul Allen in 1975.",
    }
]

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {
        "id": "doc4",
        "text": "Microsoft is a technology company that develops software. It was founded by Bill Gates and Paul Allen in 1975.",
    },
    {
        "id": "doc5",
        "text": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions.",
    },
    {
        "id": "doc6",
        "text": "Machine Learning (ML) is a subset of AI that focuses on the development of algorithms that allow computers to learn from and make predictions based on data.",
    },
    {
        "id": "doc7",
        "text": "Deep Learning is a subset of Machine Learning that uses neural networks with many layers to analyze various factors of data.",
    },
    {
        "id": "doc8",
        "text": "Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and respond to human language.",
    },
    {
        "id": "doc9",
        "text": "AI can be categorized into two types: Narrow AI, which is designed to perform a narrow task, and General AI, which can perform any intellectual task that a human can do.",
    },
    {
        "id": "doc10",
        "text": "Computer Vision is a field of AI that enables computers to interpret and make decisions based on visual data from the world.",
    },
    {
        "id": "doc11",
        "text": "Reinforcement Learning is an area of Machine Learning where an agent learns to make decisions by taking actions in an environment to achieve maximum cumulative reward.",
    },
    {
        "id": "doc12",
        "text": "The Turing Test, proposed by Alan Turing, is a measure of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.",
    },
]

def getDocs(t):
    if t == 'basic':
        return getInfo(basic_docs)
    if t == 'intermediate':
        return getInfo(intermediate_docs)
    
    return getInfo(documents)
    
def getInfo(docs):
    return (
        [doc['id'] for doc in docs],
        [doc['text'] for doc in docs]
    )