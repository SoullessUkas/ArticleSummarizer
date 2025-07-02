import streamlit as st
from utils.pdf_loader import extract_text_from_pdf
from llm.local_llm import get_llm
from langchain.chains.summarize import load_summarize_chain

st.set_page_config(page_title="Sumarizador PDF", layout="centered")
st.title("📄🔍 Sumarizador de Artigos em PDF")

uploaded_file = st.file_uploader("Envie um arquivo PDF", type="pdf")

if uploaded_file:
    raw_text, splits = extract_text_from_pdf(uploaded_file)
    st.text_area("Conteúdo extraído:", value=raw_text[:3000], height=200)

    if st.button("Gerar Resumo"):
        with st.spinner("Carregando modelo local..."):
            llm = get_llm()
            chain = load_summarize_chain(llm, chain_type="map_reduce")
            summary = chain.run(splits)

        st.subheader("Resumo Gerado:")
        st.success(summary)
