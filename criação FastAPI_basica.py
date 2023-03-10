#pip install fastapi
#pip install uvicorn

from fastapi import FastAPI

app = FastAPI()

vendas_granel = {
    1: {"produto": "oregano", "preco_100g": 2, "qtd_vendida": 10},
    2: {"produto": "paprica defumada", "preco_100g": 3.90, "qtd_vendida": 20},
    3: {"produto": "eritritol", "preco_100g": 6, "qtd_vendida": 3},
    4: {"produto": "curry", "preco_100g": 9.90, "qtd_vendida": 10},
}

@app.get("/")
def home():
    return {"Vendas aGranel": len(vendas_granel)}

@app.get("/venda/{id_venda}")
def venda(id_venda: int):
    if id_venda in vendas_granel:
        return vendas_granel[id_venda]
    else:
        return {"ERRO": "ID Venda nulo"}
