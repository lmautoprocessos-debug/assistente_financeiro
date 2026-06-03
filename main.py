import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class Transacao(BaseModel):
    descricao: str
    valor: float
    quem_gastou: str

@app.post("/gasto")
async def receber_gasto(gasto: Transacao):
    mensagem_retorno = f"Gasto de R$ {gasto.valor:.2f} com '{gasto.descricao}' registrado por {gasto.quem_gastou}!"
    return {
        "status": "sucesso",
        "mensagem": mensagem_retorno
    }

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=porta)