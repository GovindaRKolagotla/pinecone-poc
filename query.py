from pinecone import Pinecone
from utils.constants import ConstantsManagement

# Create an instance of ConstantsManagement
constants_manager = ConstantsManagement()

pc = Pinecone(api_key=constants_manager.api_key)
index_name = constants_manager.index_name
index = pc.Index(index_name)

query_results1 = index.query(
    namespace="ns1",
    vector=[1.0, 1.5],
    top_k=3,
    include_values=True
)

print(query_results1)

query_results2 = index.query(
    namespace="ns2",
    vector=[1.0,-2.5],
    top_k=3,
    include_values=True
)

print(query_results2)
