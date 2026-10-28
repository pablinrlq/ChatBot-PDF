<div align="center">

# ChatBot PDF

**Converse com qualquer PDF usando RAG.**

Você faz uma pergunta, o sistema busca os trechos certos do documento e o Gemini
responde com base só no que está escrito ali.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square&logo=meta&logoColor=white)

</div>

## Como funciona

```
PDF ──► pedaços de 1000 caracteres ──► embeddings (HuggingFace, local) ──► índice FAISS
                                                                              │
pergunta ──► busca os 3 trechos mais parecidos ◄──────────────────────────────┘
                     │
                     └──► Gemini responde usando só esses trechos
```

1. **Ingestão** (`src/ingest.py`): lê o PDF, quebra em pedaços com sobreposição de 200 caracteres
   e gera os vetores com o modelo `all-MiniLM-L6-v2`, que roda na sua máquina, sem custo.
2. **Busca:** a pergunta vira vetor e o FAISS acha os trechos mais próximos.
3. **Resposta:** os trechos entram no prompt como contexto, e o Gemini responde em cima deles.
   Isso reduz bastante a chance de o modelo inventar resposta.

Tem duas interfaces: uma web com **Streamlit** (`app_web.py`) e uma de terminal com
memória da conversa (`src/app.py`).

## Rodando

Precisa do Python 3.10+ e de uma chave gratuita do [Google AI Studio](https://aistudio.google.com/).

```bash
git clone https://github.com/pablinrlq/ChatBot-PDF.git
cd ChatBot-PDF
python -m venv .venv
.venv\Scripts\activate          # no Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz:

```env
GOOGLE_API_KEY=sua-chave-aqui
```

Coloque o PDF em `inputs/documento.pdf`, gere o índice e abra o chat:

```bash
python src/ingest.py
streamlit run app_web.py
```

Prefere o terminal? `python src/app.py`.

## Estrutura

```
├── app_web.py        interface web (Streamlit)
├── src/
│   ├── ingest.py     lê o PDF e cria o índice vetorial
│   └── app.py        chat no terminal com memória
├── inputs/           PDF de entrada
└── requirements.txt
```

## O que aprendi

- Como RAG funciona na prática: chunking, embeddings, busca vetorial e montagem do prompt
- Que dá para rodar a parte de embeddings localmente e pagar só pela geração
- Tamanho e sobreposição dos pedaços mudam muito a qualidade da resposta

---

<div align="center">
<sub>Feito por <a href="https://github.com/pablinrlq">Pablo Moises</a> · projeto do bootcamp da DIO</sub>
</div>
