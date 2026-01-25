import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Configuração da página
st.set_page_config(page_title="Chat com PDF", page_icon="📄")
st.title("🤖 Chatbot Inteligente de PDF")

load_dotenv()

# Função para carregar os recursos (cache para não recarregar toda hora)
@st.cache_resource
def carregar_recursos():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.3)
    return vectorstore, llm

try:
    vectorstore, llm = carregar_recursos()
    
    # Inicializa o histórico de mensagens no Streamlit
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostra as mensagens antigas na tela
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de entrada de texto
    if prompt_usuario := st.chat_input("Pergunte algo sobre o seu PDF..."):
        # Mostra a pergunta do usuário
        st.session_state.messages.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)

        # Lógica RAG
        with st.spinner("Buscando no PDF..."):
            docs = vectorstore.similarity_search(prompt_usuario, k=3)
            contexto = "\n".join([doc.page_content for doc in docs])
            
            prompt_final = f"Use este texto para responder: {contexto}\n\nPergunta: {prompt_usuario}"
            
            # Chama o Gemini
            resposta = llm.invoke(prompt_final)
            conteudo_resposta = resposta.content

        # Mostra a resposta da IA
        with st.chat_message("assistant"):
            st.markdown(conteudo_resposta)
        st.session_state.messages.append({"role": "assistant", "content": conteudo_resposta})

except Exception as e:
    st.error(f"Erro ao carregar o sistema: {e}")
    st.info("Certifique-se de que a pasta 'vectorstore' existe.")