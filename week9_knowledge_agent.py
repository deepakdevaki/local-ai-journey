import os, ssl, glob
from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

ssl._create_default_https_context = ssl._create_unverified_context

DOC_FOLDER = "my_docs"
os.makedirs(DOC_FOLDER, exist_ok=True)

if not glob.glob(os.path.join(DOC_FOLDER, "*.txt")):
    with open(os.path.join(DOC_FOLDER, "example.txt"), "w") as f:
        f.write("This is a sample note. Ask: What is this?")
    print("🔍 Week 9: Knowledge Agent\nCreated sample note in 'my_docs/'")

print("Run full version with ChromaDB + Phi-3 to ask questions!")