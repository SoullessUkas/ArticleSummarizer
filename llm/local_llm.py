from langchain_community.llms import LlamaCpp

def get_llm():
    return LlamaCpp(
        model_path="models/model.gguf",
        n_ctx=2048,
        temperature=0.1,
        max_tokens=512,
        verbose=False,
        n_gpu_layers=35   # 👈 QUANTAS CAMADAS VÃO PRA GPU
    )
