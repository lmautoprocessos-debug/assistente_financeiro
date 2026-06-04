from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Julius está online e ouvindo!"}

@app.post("/webhook")
async def receber_mensagem(request: Request):
    dados = await request.json()
    
    # Vamos ver o que o WhatsApp nos manda no log do Render
    # Isso vai nos ajudar a entender a estrutura da mensagem
    print("Nova mensagem recebida:", dados)
    
    # Aqui depois colocaremos a lógica:
    # 1. Se for imagem -> chama função processar_imagem_gasto
    # 2. Se for texto -> chama função analisar_comando_texto
    
    return {"status": "recebido"}