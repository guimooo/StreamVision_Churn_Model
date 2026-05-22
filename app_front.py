import os
import streamlit as st
import requests

st.set_page_config(page_title="Previsão de Churn", page_icon="📊")
st.title("📊 Previsão de Churn de Clientes")
st.write("Insira os dados do cliente para prever o risco de cancelamento.")

url_api = os.getenv("API_URL", "http://127.0.0.1:8000/predict")

with st.form("form_cliente"):
    col1, col2 = st.columns(2)
    
    with col1:
        idade = st.number_input("Idade", min_value=18, max_value=120, value=23)
        renda_mensal = st.number_input("Renda Mensal (R$)", min_value=0.0, value=2500.0)
        tenure_dias = st.number_input("Dias como cliente (Tenure)", min_value=0, value=234)
        total_pago = st.number_input("Total Pago Histórico", min_value=0.0, value=1500.0)
        ticket_medio = st.number_input("Ticket Médio", min_value=0.0, value=150.0)
        
    with col2:
        total_minutos = st.number_input("Total de Minutos Usados", min_value=0.0, value=1000.0)
        media_minutos = st.number_input("Média de Minutos", min_value=0.0, value=100.0)
        consumo_recente = st.number_input("Consumo Recente", min_value=0.0, value=50.0)
        minutos_por_dia_ativo = st.number_input("Minutos por Dia Ativo", min_value=0.0, value=30.0)
        pct_consumo_Documentario = st.number_input("% Consumo de Documentários", min_value=0.0, max_value=100.0, value=15.0)
        pct_consumo_Infantil = st.number_input("% Consumo de Infantil", min_value=0.0, max_value=100.0, value=10.0)
        diversificacao_categoria = st.number_input("Diversificação de Categorias", min_value=0.0, value=3.0)
        
    submit_button = st.form_submit_button(label="🔮 Prever Risco")

if submit_button:
    dados_para_api = {
        "idade": int(idade),
        "renda_mensal": float(renda_mensal),
        "tenure_dias": int(tenure_dias),
        "total_pago": float(total_pago),
        "ticket_medio": float(ticket_medio),
        "total_minutos": float(total_minutos),
        "media_minutos": float(media_minutos),
        "consumo_recente": float(consumo_recente),
        "minutos_por_dia_ativo": float(minutos_por_dia_ativo),
        "pct_consumo_Documentario": float(pct_consumo_Documentario),
        "pct_consumo_Infantil": float(pct_consumo_Infantil),
        "diversificacao_categoria": float(diversificacao_categoria)
    }

    try:
        with st.spinner('Analisando perfil do cliente...'):
            resposta = requests.post(url_api, json=dados_para_api, timeout=10)
            
            if resposta.status_code == 200:
                resultado = resposta.json()
                if resultado["churn"]:
                    st.error(f"⚠️ {resultado['mensagem']}")
                else:
                    st.success(f"✅ {resultado['mensagem']}")
            else:
                st.warning(f"Erro na API. Status Code: {resposta.status_code}")
                st.write(resposta.json())
                
    except requests.exceptions.ConnectionError:
        st.error(f"Erro de conexão: não foi possível alcançar a API em {url_api}. O container da API está rodando?")
    except requests.exceptions.Timeout:
        st.error("Tempo limite excedido. A API demorou muito para responder.")
