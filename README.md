# Focus API

API para registro e diagnóstico de produtividade baseada em níveis de foco e tempo de estudo.

---

## 🚀 Tecnologias

- Python 3.13
- FastAPI
- SQLModel
- SQLAlchemy (async)
- SQLite (dev)
- uv (package manager)
- Docker

---

## 📦 Requisitos

Antes de rodar o projeto:

- Python 3.13+
- uv instalado (0.11.11)
- Docker (29.4.2)
- Sqlite3 (3.51.0)

---

## ⚙️ Instalação local

### 1. Clonar o projeto

```bash
git clone <repo-url>
cd teste-tecnico-python-backend
````

---

### 2. Instalar dependências

```bash
uv sync
```

---

### 3. Rodar a aplicação

```bash
uv run uvicorn src.main:app --reload --port 8000
```

API estará disponível em:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## 🗄️ Banco de dados

O projeto usa SQLite por padrão.

O arquivo será criado automaticamente:

```
database.db
```

---

## 🧪 Rodando testes

```bash
uv run pytest
```

---

## 🐳 Rodando com Docker

### 1. Build da imagem

```bash
docker build -t focus-api .
```

### 2. Rodar container

```bash
docker run -p 8000:8000 focus-api
```

---

## 📌 Endpoints

### Criar registro de foco

```http
POST /registro-foco
```

Exemplo:

```json
{
  "nivel_foco": 4,
  "tempo_minutos": 30,
  "comentario": "estudando pytest"
}
```

---

### Diagnóstico de produtividade

```http
GET /diagnostico-produtividade
```

Retorna:

```json
{
  "media_nivel_foco": 4.2,
  "tempo_total_focado": 210,
  "mensagem_feedback": "Seu foco está afiado como uma katana."
}
```

---

## 🧪 Estratégia de testes

O projeto utiliza:

* pytest
* pytest-asyncio
* TestClient (FastAPI)
* SQLite em memória (quando aplicável)
* mocks para repositórios

---

## 🧠 Arquitetura

```
Controllers → Services → Repositories → Database
```

Separação em camadas para facilitar testes e manutenção.

---

## 📌 Observações

* O projeto usa `uv` como gerenciador de dependências
* SQLModel com async session
* Estrutura pensada para fácil evolução para PostgreSQL
