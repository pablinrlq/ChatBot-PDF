# ChatBot PDF Inteligente (RAG)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

Este projeto é um assistente virtual de alta performance que utiliza a técnica de **RAG (Retrieval-Augmented Generation)** para conversar com arquivos PDF. O sistema lê o documento, compreende o contexto e responde perguntas de forma precisa utilizando a inteligência artificial do Google.

---

## Tecnologias Utilizadas

O projeto foi construído utilizando as ferramentas mais modernas do ecossistema de IA:

* **Linguagem:** [Python 3.10+](https://www.python.org/)
* **Interface Web:** [Streamlit](https://streamlit.io/) (UI reativa e amigável)
* **Modelo de Linguagem (LLM):** [Google Gemini 1.5 Flash](https://aistudio.google.com/)
* **Orquestração de IA:** [LangChain](https://www.langchain.com/) (Integração de dados e memória)
* **Banco de Dados Vetorial:** [FAISS](https://github.com/facebookresearch/faiss) (Busca semântica ultra rápida)
* **Embeddings:** [HuggingFace](https://huggingface.co/) (`all-MiniLM-L6-v2`)
* **Processamento de PDF:** [PyPDF](https://pypi.org/project/pypdf/)

---

## O que é RAG?

Neste projeto, implementamos o **RAG (Retrieval-Augmented Generation)**, que resolve o problema de "alucinação" das IAs tradicionais. O fluxo funciona assim:

1.  **Recuperação (Retrieval):** Quando você faz uma pergunta, o sistema busca nos "vetores" do FAISS os trechos exatos do seu PDF que contêm a resposta.
2.  **Aumentação (Augmentation):** O sistema anexa esses trechos como um "contexto de segurança" para a IA.
3.  **Geração (Generation):** O **Gemini 1.5 Flash** lê o contexto e gera uma resposta baseada estritamente nos dados reais do seu arquivo.

---

```bash

👤 Autor
Desenvolvido com ☕ e Python por Pablo.

Nota: Este projeto foi criado para demonstrar a aplicação prática de NLP (Processamento de Linguagem Natural) e integração com APIs de modelos de linguagem de larga escala (LLMs) como proposta da escola de cursos DIO.
