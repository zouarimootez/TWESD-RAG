from langchain_ollama import OllamaEmbeddings #pour générer les embeddings via ton modèle mxbai-embed-large
from langchain_chroma import Chroma #base vectorielle (VectorStore)
from langchain_core.documents import Document #structure des documents LangChain
import os   #vérifier si la base existe déjà
import pandas as pd #lire le CSV 

df = pd.read_csv("stm32f103_dataset.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large") #Tu utilises mxbai-embed-large pour transformer tes documents en vecteurs.

db_location = "./chrome_langchain_db0"
add_documents = not os.path.exists(db_location)
#✔ Si la base n’existe pas, on va l’initialiser et ajouter les documents.
#✔ Si elle existe déjà, on ne régénère pas tout (gain de temps).
if add_documents:
    documents = [] #Page,Chunk,Text,Metadata
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content = str(row["Page"]) + " " + str(row["Metadata"]),
            metadata={"Text": row["Text"], "Chunk": row["Chunk"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document) #Chaque ligne du CSV devient un Document LangChain
        
vector_store = Chroma(
    collection_name="reviewers", #nom de ta base vectorielle
    persist_directory=db_location, #où elle est sauvegardée
    embedding_function=embeddings #modèle utilisé pour créer les vecteurs (mxbai)
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids) #générer l’embedding stocker le vecteur + metadata + id
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
) # crée un retriever qui retourne les 5 vecteurs les plus proches d’une requête