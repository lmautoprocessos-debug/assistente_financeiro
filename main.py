import os
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client

app = FastAPI()

# -------------------------------------------------------------------
# CONFIGURAÇÃO DO BANCO DE DADOS (SUPABASE)
# Substitua com os dados reais que você copiou do painel do Supabase!
# -------------------------------------------------------------------
SUPABASE_URL = "https://llgxgrhhnswamjcbnrzj.supabase.co"
SUPABASE_KEY = "sb_publishable_6w4Wutprhxg7Sj7wBbT_0w_EKHv6CZt"

# Inicializa o cliente para conectar ao Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# -------------------------------------------------------------------
# MODELO DE DADOS (O que a API vai esperar receber no Swagger/Robô)
# -------------------------------------------------------------------
class Transacao(BaseModel):
    descricao: str
    valor: float
    quem_gastou: str
    com_quem_gasto: str = ""  # Deixamos como opcional com um valor padrão vazio


# -------------------------------------------------------------------
# ROTA DA API (POST /gasto)
# -------------------------------------------------------------------
@app.post("/gasto")
def registrar_gasto(transacao: Transacao):
    try:
        # Prepara o dicionário mapeando os dados recebidos para as
        # colunas exatas que você criou na tabela do Supabase
        dados_gasto = {
            "descricao_gasto": transacao.descricao,
            "valor_gasto": transacao.valor,
            "com_quem_gasto": transacao.com_quem_gasto,
            "quem_gastou": transacao.quem_gastou
        }
        
        # Faz a inserção real na tabela 'gastos' do seu banco de dados
        resposta = supabase.table("Gastos").insert(dados_gasto).execute()
        
        return {
            "status": "sucesso",
            "mensagem": f"Gasto de R$ {transacao.valor:.2f} com '{transacao.descricao}' salvo com sucesso no Julius!",
            "dados_salvos": resposta.data
        }
        
    except Exception as e:
        return {
            "status": "erro",
            "mensagem": f"Falha ao salvar no banco de dados: {str(e)}"
        }