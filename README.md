# Sumarizador de Artigos PDF com LLM Local

Este aplicativo permite fazer upload de arquivos PDF e gerar um resumo do conteúdo utilizando uma LLM leve localmente com `llama-cpp-python`.

## Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Coloque seu modelo `.gguf` em `models/model.gguf`.

3. Execute com:
```bash
streamlit run app.py
```

## Requisitos

- Python 3.9+
- Modelo `.gguf` (ex: Mistral, TinyLlama)
