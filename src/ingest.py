import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def processar_documentos():
    pdf_path = "inputs/documento.pdf"
    
    if not os.path.exists(pdf_path):
        print("❌ ERRO: Coloque um arquivo chamado 'documento.pdf' na pasta 'inputs'.")
        return

    print(f"📄 Lendo o arquivo: {pdf_path}...")
    loader = PyPDFLoader(pdf_path)
    documentos = loader.load()

    # Quebrando o texto em pedaços menores (Chunks)
    print("✂️  Fatiando o documento...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documentos)
    print(f"   -> Gerados {len(chunks)} fragmentos de texto.")

    # Embeddings rodam localmente com HuggingFace, sem custo de API
    print("🧠 Gerando Embeddings com HuggingFace (100% Local)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Criando o banco vetorial
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # Salvando no disco
    vectorstore.save_local("vectorstore")
    print("✅ Banco de dados vetorial salvo com sucesso na pasta 'vectorstore'!")

if __name__ == "__main__":
    processar_documentos()