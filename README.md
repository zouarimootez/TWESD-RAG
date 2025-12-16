# 📘 Document RAG-Based Technical Assistant (LangChain + Ollama)

This project implements a **Retrieval-Augmented Generation (RAG)** system designed to answer **technical questions about the STM32F103 microcontroller** using official documentation (PDF) and a **local LLM via Ollama**.

The system combines:

* PDF document processing
* Vector embeddings with **mxbai-embed-large**
* A **Chroma** vector database
* A **local LLM (llama3.2)** for accurate, context-aware responses

---

## 🧠 Project Architecture

```
PDF (STM32F103 Reference Manual)
        ↓
Text Extraction & Chunking
        ↓
CSV Dataset Generation
        ↓
Embeddings (mxbai-embed-large)
        ↓
Chroma Vector Store
        ↓
Retriever (Top-K similarity search)
        ↓
LLM (llama3.2 via Ollama)
        ↓
Interactive Technical Q&A
```

---

## 📂 Project Structure

```
.
├── vet.py                 # Extracts text from PDF and builds CSV dataset
├── rag.py                 # Builds embeddings, vector store, and retriever
├── test.py                # Interactive RAG-based chatbot
├── stm32f103_dataset.csv  # Generated dataset (chunks + metadata)
├── chrome_langchain_db0/  # Persistent Chroma vector database
├── STM32F103.PDF          # Initial reference manual document
└── README.md
```

---

## 🔑 Requirements

* Python **3.10+** 
* Ollama installed and running locally

---

## 🛠️ Installation & Setup : Create Virtual Environment


Create and activate a Python virtual environment, then install dependencies:

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```


### Ollama Models

Make sure the following models are pulled:

```bash
ollama pull mxbai-embed-large
ollama pull llama3.2
```

---

## 📄 Step 1: Convert PDF to CSV Dataset

The script extracts text from the STM32F103 PDF, splits it into overlapping chunks, and stores everything in a CSV file.

**Key parameters**

* `CHUNK_SIZE = 1000`
* `CHUNK_OVERLAP = 200`

```bash
python vet.py
```

Output:

```
stm32f103_dataset.csv
```

Each row contains:

* Page number
* Chunk index
* Text content
* Metadata

---

## 🔎 Step 2: Build Vector Database (RAG)

This step:

* Loads the CSV dataset
* Generates embeddings using **mxbai-embed-large**
* Stores vectors in a **persistent Chroma database**
* Avoids recomputation if the database already exists

```bash
python rag.py
```

✔ Uses local embeddings  
✔ Fast restart thanks to persistence  
✔ Optimized for embedded documentation search

---

## 🤖 Step 3: Run the Interactive Chatbot

The chatbot:

* Retrieves the **top-5 most relevant chunks**
* Injects them into a structured technical prompt
* Uses **llama3.2** to generate precise answers

```bash
python chat.py
```

Example:

```
Ask your question (q to quit): What is the flash memory size of STM32F103C8?
```

---

## 🧪 Prompt Design

The assistant is instructed to:

* Act as an **STM32 expert**
* Give **concise, structured, and technical answers**
* Reference peripherals, memory, and hardware architecture
* Make reasonable assumptions if the question is ambiguous

This ensures **engineering-grade answers**, not generic LLM output.

---

## 🚀 Key Features

* ✅ Fully **offline / local AI**
* ✅ Accurate answers grounded in official documentation
* ✅ Persistent vector database (fast startup)
* ✅ Modular & extensible RAG pipeline
* ✅ Suitable for embedded engineers and students

---

## 🔧 Possible Extensions

* Add **source citations** in answers
* Deploy as a **Web API (FastAPI / WebSocket)**
* Integrate with **Raspberry Pi**
* Support multiple STM32 families
* Add conversational memory

---

## 📧 Contact

For questions or suggestions, feel free to reach out:

- 📧 **Email**: [zouarimootez@gmail.com](mailto:zouarimootez@gmail.com)
- 💼 **LinkedIn**: [linkedin.com/in/mootez-zouari](https://linkedin.com/in/mootez-zouari/)
- 🌐 **Portfolio**: [mootezzouari.netlify.app](https://mootezzouari.netlify.app/)

You can also open an issue on GitHub for bugs or feature requests.
