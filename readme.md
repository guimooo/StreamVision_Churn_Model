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

### 5. Parar os containers
```bash
docker compose down
```

### 6. Parar e remover volumes
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