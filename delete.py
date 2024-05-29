
from pinecone import Pinecone
from utils.constants import ConstantsManagement

# Create an instance of ConstantsManagement
constants_manager = ConstantsManagement()

pc = Pinecone(api_key=constants_manager.api_key)

index_name = constants_manager.index_name
pc.delete_index(index_name)