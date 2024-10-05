from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline

# Initialize in-memory document store with BM25 enabled
document_store = InMemoryDocumentStore(use_bm25=True)

# Add sample documents
data = """The discovery of the apple as we know it is not attributed to a single event, 
         but rather, apples have been cultivated and consumed for thousands of years. Apples originated
          in Central Asia, specifically in the Tian Shan mountains in Kazakhstan. The wild ancestor of today's 
         domestic apples, Malus sieversii, grew in this region. Over time, apples spread through trade routes to
          Europe and the rest of the world. Various breeding and cultivation techniques have led to the diverse varieties 
         of apples we enjoy today. The story of apples also carries symbolism in various cultures and myths, such as the well-known 
         story of Isaac Newton, though the discovery of gravity is not tied to the actual discovery of the fruit."""
docs = [{"content": 
         
         data
         
         
         }]
document_store.write_documents(docs)

# Initialize retriever and reader
retriever = BM25Retriever(document_store=document_store)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")

# Create pipeline
pipe = ExtractiveQAPipeline(reader, retriever)

# Ask a question
question = "How did apples spread throughout the world?"
result = pipe.run(query=question, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 5}})
print(result)











### ouput
'''
  warnings.warn(
he rest of the world. Various breeding and cultivation techniques have led to the diverse varieties of apples we enjoy',
'offsets_in_document': [{'start': 412, 'end': 455}], 'offsets_in_context': [{'start': 54, 'end': 97}], 'document_ids': ['297ea9772f2b2b63b236429a8107970b'],
'meta': {}}>], 'documents': [<Document: {'content': "The discovery of the apple as we know it is not attributed to a single event, but rather, apples have been 
cultivated and consumed for thousands of years. Apples originated in Central Asia, specifically in the Tian Shan mountains in Kazakhstan. The wild ancestor of 
today's domestic apples, Malus sieversii, grew in this region. Over time, apples spread through trade routes to Europe and the rest of the world. Various breeding 
and cultivation techniques have led to the diverse varieties of apples we enjoy today. The story of apples also carries symbolism in various cultures and myths, 
such as the well-known story of Isaac Newton, though the discovery of gravity is not tied to the actual discovery of the fruit.", 
'content_type': 'text', 'score': 0.47583065467091573, 'meta': {}, 'id_hash_keys': ['content'], 'embedding': None, 'id': '297ea9772f2b2b63b236429a8107970b'}>],
'root_node': 'Query', 'params': {'Retriever': {'top_k': 5}, 'Reader': {'top_k': 5}}, 'node_id': 'Reader'}
'''
