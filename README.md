# Small Backend Service

A stateless, production-ready microservice built with **Python 3.13**, **FastAPI**, and managed by the **uv** package manager.

## 🚀 Key Features

-   **High Performance**: Powered by FastAPI, built on top of Starlette and Pydantic.
-   **Modern Tooling**: Managed by `uv` for lightning-fast dependency resolution and virtual environment management.
-   **Strict Validation**: Uses Pydantic v2 for data validation and settings management.
-   **Security**: Includes utilities for JWT token generation and bcrypt password hashing.
-   **Production Ready**: Modular structure, structured logging (standard), and optimized multi-stage Docker builds.
-   **API Versioning**: Pre-configured with `/v1` prefix for easy evolution.

## 🛠 Tech Stack

-   **Runtime**: Python 3.13
-   **Package Manager**: [uv](https://github.com/astral-sh/uv)
-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Validation**: [Pydantic v2](https://docs.pydantic.dev/latest/)
-   **Security**: `python-jose`, `passlib`

---

## 📂 Project Structure

```text
small-backend/
├── app/
│   ├── main.py              # Application entry point & health checks
│   ├── api/
│   │   └── v1/
│   │       ├── api.py       # Main router for V1
│   │       └── endpoints/   # Individual endpoint logic (items, utils)
│   ├── core/
│   │   ├── config.py        # Settings and environment variables
│   │   └── security.py      # JWT and hashing utilities
│   └── schemas/             # Pydantic models for validation
├── tests/                   # Automated test suite
├── Dockerfile               # Optimized multi-stage build
├── docker-compose.yml       # Dev/Prod orchestration
└── pyproject.toml           # Project dependencies
```

---

## 🎬 Getting Started

### Prerequisites

-   [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

### Local Installation

1.  **Clone the repository** (if applicable).
2.  **Sync dependencies**:
    ```bash
    uv sync
    ```
3.  **Run the application**:
    ```bash
    uv run uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

---

## 🐳 Docker Usage

This project is optimized for containerization using a multi-stage Dockerfile.

### Build and Run with Docker Compose

```bash
docker-compose up --build
```

### Build Image Manually

```bash
docker build -t small-backend .
docker run -p 8000:8000 small-backend
```

---

## 📖 API Documentation

Once the service is running, you can explore the API using the interactive documentation:

-   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
-   **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Summary of Endpoints

| Method | Path | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Service health status |
| `GET` | `/v1/version` | Returns API version and name |
| `POST` | `/v1/get-token` | Generates a mock JWT token |
| `GET` | `/v1/info` | Mock system information |
| `POST` | `/v1/echo` | Echoes back the JSON body for testing |
| `GET` | `/v1/users/me` | Returns mock info for current user |
| `GET` | `/v1/items` | List all mock items |
| `POST` | `/v1/items` | Add a new mock item |
| `GET` | `/v1/items/{id}` | Get a specific item by ID |

---

## ☸️ Helm Deployment

A Helm chart is provided in the `helm/small-backend` directory for deploying to Kubernetes.

### Linting and Templating

```bash
# Lint the chart
helm lint helm/small-backend

# Render templates locally
helm template helm/small-backend
```

### Installing the Chart

```bash
# Install/Upgrade the chart
helm upgrade --install small-backend helm/small-backend --namespace default
```

---

## 🧪 Testing

The project uses `pytest` and `httpx` for automated testing.

```bash
# Run all tests
uv run pytest

# Run with coverage (if installed)
uv run pytest --cov=app
```

---

## ⚙️ Configuration

The application uses `pydantic-settings` to manage configuration. You can override settings via environment variables:

-   `PROJECT_NAME`: Name of the application.
-   `SECRET_KEY`: Used for JWT encryption (Change this in production!).
-   `ACCESS_TOKEN_EXPIRE_MINUTES`: Token lifespan.

Example:
```bash
export SECRET_KEY="your-production-secret"
uv run uvicorn app.main:app
```
