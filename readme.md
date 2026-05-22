# 🐳 Docker — Sistema de Previsão de Churn

## Estrutura dos arquivos

```
projeto/
├── Dockerfile            # Container principal (API FastAPI)
├── Dockerfile.frontend   # Container de apoio (Dashboard Streamlit)
├── docker-compose.yml    # Orquestração dos dois containers
├── .env                  # Variáveis de ambiente
├── api.py                # Código da API
├── app_front.py          # Código do frontend (MODIFICADO)
├── requirements.txt      # Dependências Python
└── modelo_churn.pkl      # Modelo treinado (necessário!)
```

---

## Como executar


### 1. Subir os dois containers
```bash
docker compose up --build
```

### 2. Acessar as aplicações
| Serviço   | URL                          |
|-----------|------------------------------|
| Dashboard | http://localhost:8501        |
| API docs  | http://localhost:8000/docs   |
| API JSON  | http://localhost:8000/predict|

* Para testar o predict via terminal (bash):

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "idade": 30,
    "renda_mensal": 3000.0,
    "tenure_dias": 365,
    "total_pago": 2000.0,
    "ticket_medio": 150.0,
    "total_minutos": 1200.0,
    "media_minutos": 100.0,
    "consumo_recente": 60.0,
    "minutos_por_dia_ativo": 40.0,
    "pct_consumo_Documentario": 20.0,
    "pct_consumo_Infantil": 5.0,
    "diversificacao_categoria": 3.0
  }'
```

### 3. Parar os containers
```bash
docker compose down
```

### 4. Parar e remover volumes
```bash
docker compose down -v
```

---

## Comandos úteis

```bash
# Ver logs de todos os containers
docker compose logs -f

# Ver logs só da API
docker compose logs -f api

# Ver logs só do frontend
docker compose logs -f frontend

# Rebuildar apenas um serviço
docker compose up --build api

# Ver status dos containers
docker compose ps
```

---