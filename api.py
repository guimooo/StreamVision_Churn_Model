from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="API de Previsão de Churn",
    description="Endpoint para prever o cancelamento de clientes baseado no modelo XGBoost."
)

modelo = joblib.load('modelo_churn.pkl')

# Exatamente as 12 colunas na grafia exigida pelo erro do modelo
class ClienteData(BaseModel):
    idade: int
    renda_mensal: float
    tenure_dias: int
    total_pago: float
    ticket_medio: float
    total_minutos: float
    media_minutos: float
    consumo_recente: float
    minutos_por_dia_ativo: float
    pct_consumo_Documentario: float
    pct_consumo_Infantil: float
    diversificacao_categoria: float

@app.post("/predict")
def prever_churn(cliente: ClienteData):
    dados_dicionario = cliente.model_dump()
    
    # Criando o DataFrame com as colunas minúsculas exatas
    df_cliente = pd.DataFrame([dados_dicionario])
    
    try:
        # Agora o DataFrame casa perfeitamente com os nomes esperados
        previsao = modelo.predict(df_cliente)
        resultado = int(previsao[0])
        
        if resultado == 1:
            return {"churn": True, "mensagem": "Alerta: Alto risco de cancelamento!"}
        else:
            return {"churn": False, "mensagem": "Cliente seguro. Baixo risco."}
            
    except Exception as e:
        return {"churn": False, "mensagem": f"Erro na inferência do modelo: {str(e)}"}