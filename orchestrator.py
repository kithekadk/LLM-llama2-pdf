import chromadb
from dotenv import load_dotenv
load_dotenv()

from loader import load_directory, web_page_reader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index.embeddings import LangchainEmbedding
import torch
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import OpenAIAgent
from llama_index.llms import ChatMessage, MessageRole

remote_db = chromadb.HttpClient()

#creating the collection
collection = remote_db.get_or_create_collection(
    name = "medassist"
)

documents = load_directory() + web_page_reader()

#device configuration
device = "cuda" if torch.cuda.is_available() else "cpu"

embed_model = LangchainEmbedding(
    HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", 
        model_kwargs={"device": device}
        )
)

service_context = ServiceContext.from_defaults(embed_model=embed_model)

vectorstore = ChromaVectorStore(chroma_collection=collection)

storage_context = StorageContext.from_defaults(vector_store=vectorstore)

index = VectorStoreIndex.from_documents(
    documents=documents,
    storage_context=storage_context,
    service_context=service_context
)

query_engine = index.as_query_engine(
    top_k = 5
)

tool_metadata = ToolMetadata(
    name = "MedAssistKnowledgebase",
    description = """ 
        Use this tool to get information on Sickle Cell anaemia in Kenya"""
)

tool = QueryEngineTool(
    query_engine = query_engine,
    metadata= tool_metadata
)

SYSTEM_PROMPT = '''
    You are a friendly and coincise AI Assistant that helps people with Sickle Cell Anaemia
'''

def format_chat_history(chat_history):
    chat_objects=[]
    for i, chat in enumerate(chat_history):
        role= MessageRole.USER if i % 2 ==0 else MessageRole.ASSISTANT
        chat_object = ChatMessage(role=role, content=chat)
        chat_objects.append(chat_object)
    return chat_objects


def generate_agent(chat_history=[]):
    chat_objects = format_chat_history(chat_history)
    agent = OpenAIAgent.from_tools(
        tools= [tool],
        system_prompt= SYSTEM_PROMPT,
        chat_history=chat_objects,
        verbose=True
    )

    return agent

# query_engine.query("What can we declare")