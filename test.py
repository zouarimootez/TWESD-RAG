from langchain_ollama.llms import OllamaLLM #permet d’utiliser un modèle LLM local (ici llama3.2) via Ollama. 
from langchain_core.prompts import ChatPromptTemplate #sert à construire un prompt flexible avec des variables.
from rag import retriever #importé depuis ton fichier rag.py, utilisé pour récupérer des passages pertinents (RAG)

model = OllamaLLM(model="llama3.2")

#template = """
#You are an exeprt in answering questions about stm32f103 board

#Here are some relevant reviews: {reviews}

#Here is the question to answer: {question}
#"""
#Ce texte définit comment le LLM doit répondre.
#Il comprend deux variables : {reviews} = informations récupérées par le retriever

#{question} = question posée par l’utilisateur

# Le prompt guide le modèle pour répondre comme un expert STM32F103.


template = """
You are a highly knowledgeable expert in STM32 microcontrollers, specifically the STM32F103 family.
Your role is to provide clear, precise, and technically accurate answers.

When responding:
- Use concise and well-structured explanations.
- Refer to hardware specifications, peripherals, memory architecture, and common development workflows when relevant.
- Provide practical guidance, examples, and best practices suited for embedded engineers.
- If the question is unclear, briefly state the assumptions you make.

Below are some relevant reviews and contextual information:
{reviews}

Here is the question you must answer:
{question}

Provide the best possible technical answer based on your expertise and the given context.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model #on prend le prompt, on l’envoie comme entrée au modèle. La sortie = réponse du modèle

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    reviews = retriever.invoke(question) #Le retriever cherche des passages liés à la question :
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)