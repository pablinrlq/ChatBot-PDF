import os
from dotenv import load_dotenv

# Imports mais estáveis para evitar o erro "No module named langchain.chains"
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain # Tente voltar para o simples
from langchain.memory import ConversationBufferMemory

# Carrega as variáveis do arquivo .env
load_dotenv()

def iniciar_chat():
    # 1. Verificações Iniciais
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ Erro: GOOGLE_API_KEY não encontrada no .env")
        return

    if not os.path.exists("vectorstore"):
        print("❌ Erro: Pasta 'vectorstore' não encontrada. Rode o script de ingestão primeiro!")
        return

    print("🔄 Carregando banco de dados e IA...")

    try:
        # 2. Configura Embeddings (o "tradutor" de texto para números)
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # 3. Carrega o banco de dados FAISS
        # allow_dangerous_deserialization é necessário para carregar arquivos .pkl locais
        vectorstore = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

        # 4. Configura o Gemini (modelo 1.5-flash)
        llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.3)

        # 5. Configura a Memória do Chat
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # 6. Cria a estrutura RAG (Retrieval-Augmented Generation)
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )

        print("\n" + "="*50)
        print("🤖 CHATBOT PRONTO! (Digite 'sair' para encerrar)")
        print("="*50 + "\n")

        # 7. Loop de conversa
        while True:
            pergunta = input("Você: ")
            
            if pergunta.lower() in ["sair", "exit", "quit"]:
                print("👋 Até logo!")
                break

            if not pergunta.strip():
                continue

            try:
                # Chama a IA para buscar no PDF e responder
                resultado = qa_chain.invoke({"question": pergunta})
                print(f"\nAI: {resultado['answer']}\n")
            except Exception as e:
                print(f"\n❌ Erro ao processar pergunta: {e}")

    except Exception as e:
        print(f"❌ Erro crítico ao iniciar: {e}")

if __name__ == "__main__":
    iniciar_chat()