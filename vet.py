import pandas as pd
from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

PDF_PATH = Path("D:/chatbot/aaa/stm32f103.pdf")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
OUTPUT_CSV = "stm32f103_dataset.csv"

# Lire le PDF
reader = PdfReader(str(PDF_PATH))
docs = []
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    if text:
        docs.append(Document(page_content=text.strip(), metadata={"page": i}))

# Découper en chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
chunks = splitter.split_documents(docs)

# Construire le dataset
data = []
for i, chunk in enumerate(chunks, start=1):
    data.append({
        "Page": chunk.metadata["page"],
        "Chunk": i,
        "Text": chunk.page_content,
        "Metadata": chunk.metadata
    })

# Sauvegarder en CSV
df = pd.DataFrame(data)
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Dataset saved to {OUTPUT_CSV}")
