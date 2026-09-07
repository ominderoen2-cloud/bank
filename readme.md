# Banking API

A production-oriented RESTful banking API built with **Python, Flask, and PostgreSQL**. The project started as a layered backend application and evolved into a containerized, CI/CD-enabled Kubernetes deployment.

It demonstrates backend engineering and cloud-native fundamentals including layered architecture, automated testing, Docker, GitHub Actions, GitHub Container Registry, Kubernetes, NGINX Ingress, configuration management, secrets, persistent storage, scaling, self-healing, rolling deployments, and rollbacks.

---

## Architecture

```text
                         Client
                           │
                           ▼
                   NGINX Ingress
                   bank-ingress
                           │
                           ▼
                  bank-api Service
                    ClusterIP :80
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Pod :5000     Pod :5000     Pod :5000
             │             │             │
             └────────── 5 replicas ─────┘
                           │
                           ▼
                    PostgreSQL Service
                       :5432
                           │
                           ▼
                     Postgres Pod
                           │
                           ▼
                     postgres-pvc
                        1 GiB
```

---

## Features

### Banking API

- User registration and login
- Fixed account management
- Junior account management
- Premium account management
- Transaction management
- Input validation
- PostgreSQL persistence
- Layered architecture: **Routes → Services → Repositories**
- Automated tests with Pytest

### Cloud & DevOps

- Docker containerization
- Docker Compose for local multi-container development
- GitHub Actions CI/CD
- Automated Pytest execution
- Docker image publishing to GitHub Container Registry (GHCR)
- Commit-SHA image tagging for traceable deployments
- Kubernetes deployment with Kind
- Kubernetes ConfigMaps and Secrets
- Kubernetes Service discovery
- NGINX Ingress routing
- Persistent PostgreSQL storage using a PVC
- Kubernetes self-healing
- Horizontal scaling from 3 to 5 API replicas
- Rolling updates
- Deployment rollbacks
- Kubernetes resource and event inspection

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend language |
| Flask | REST API framework |
| PostgreSQL | Relational database |
| Psycopg2 | PostgreSQL driver |
| Pytest | Automated testing |
| Docker | Containerization |
| Docker Compose | Local orchestration |
| GitHub Actions | CI/CD |
| GitHub Container Registry | Container image registry |
| Kubernetes | Container orchestration |
| Kind | Local Kubernetes cluster |
| NGINX Ingress | HTTP routing |
| Terraform | Infrastructure as Code |
| Git & GitHub | Version control |

---

## Project Structure

```text
bank/
│
├── .github/
│   └── workflows/
├── K8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-service.yaml
│   ├── secret.yaml
│   └── service.yaml
├── models/
├── repositories/
├── routes/
├── services/
├── validators/
├── tests/
├── terraform/
├── app.py
├── connect_db.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## API Endpoints

### Health

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API status |
| GET | `/health` | Health check |

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a user |
| POST | `/login` | Authenticate a user |

### Fixed Accounts

| Method | Endpoint | Description |
|---|---|---|
| POST | `/fixed` | Create account |
| GET | `/fixed` | List accounts |
| GET | `/fixed/account_number/<account_number>` | Get account by account number |
| GET | `/fixed/id/<national_id>` | Get account by national ID |
| PUT | `/fixed/<account_number>` | Update account |
| DELETE | `/fixed/<account_number>` | Delete account |

### Junior Accounts

| Method | Endpoint | Description |
|---|---|---|
| POST | `/junior` | Create account |
| GET | `/junior` | List accounts |
| GET | `/junior/account_number/<account_number>` | Get account |
| GET | `/junior/birth_certificate/<birth_certificate_number>` | Get account by birth certificate |
| PUT | `/junior/<account_number>` | Update account |
| DELETE | `/junior/<account_number>` | Delete account |

### Premium Accounts

| Method | Endpoint | Description |
|---|---|---|
| POST | `/premium` | Create account |
| GET | `/premium` | List accounts |
| GET | `/premium/account_number/<account_number>` | Get account |
| GET | `/premium/national_id/<national_id>` | Get account by national ID |
| PUT | `/premium/<account_number>` | Update account |
| DELETE | `/premium/<account_number>` | Delete account |

### Transactions

| Method | Endpoint | Description |
|---|---|---|
| POST | `/trans` | Create transaction |
| GET | `/trans` | List transactions |
| GET | `/trans/trans_id/<transaction_id>` | Get transaction |
| PUT | `/trans/send/<transaction_id>` | Send transaction |
| PUT | `/trans/recieve/<transaction_id>` | Receive transaction |

---

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/ominderoen2-cloud/bank.git
cd bank
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

The application reads its database configuration from environment variables.

Example:

```text
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/bank
```

Do not commit real credentials or secrets to the repository.

### 5. Run the API

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## Docker

Build the image:

```bash
docker build -t bank-api .
```

Run the application with Docker Compose:

```bash
docker compose up --build
```

Stop the containers:

```bash
docker compose down
```

---

## Testing

Run the complete test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Current test status:

- **28 tests passing**
- **0 warnings**

The tests cover CRUD operations, validation, API behavior, and database interactions.

---

## CI/CD

GitHub Actions automatically runs the test suite on pushes to the `main` branch.

The CI/CD pipeline:

1. Starts a PostgreSQL 16 service.
2. Checks out the repository.
3. Sets up Python.
4. Installs dependencies.
5. Runs Pytest.
6. Builds the Docker image.
7. Publishes the image to GitHub Container Registry.
8. Tags images using the Git commit SHA for traceability.

This creates a reproducible path from a code change to a versioned container image.

---

## Kubernetes

The application can be deployed to a local Kubernetes cluster using **Kind**.

The Kubernetes configuration is located in `K8s/` and includes:

- Deployment
- Service
- NGINX Ingress
- ConfigMap
- Secret
- PostgreSQL Deployment
- PostgreSQL Service
- PersistentVolumeClaim

### Create the cluster

```bash
kind create cluster --name bank
```

### Install the NGINX Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

### Apply the Kubernetes resources

```bash
kubectl apply -f K8s/
```

### Inspect the deployment

```bash
kubectl get pods
kubectl get svc
kubectl get deployment
kubectl get ingress
```

### Scale the API

```bash
kubectl scale deployment bank-api --replicas=5
```

### Monitor a rollout

```bash
kubectl rollout status deployment bank-api
```

### View rollout history

```bash
kubectl rollout history deployment bank-api
```

### Roll back a deployment

```bash
kubectl rollout undo deployment bank-api
```

### Inspect cluster events

```bash
kubectl get events --sort-by=.lastTimestamp
```

### Access the API through the Ingress

For the local Kind setup, the NGINX Ingress Controller can be exposed with port forwarding:

```bash
kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80
```

Then test:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
```

---

## Kubernetes Capabilities Demonstrated

This project was used to demonstrate real Kubernetes operational behavior rather than only writing manifests:

- **Self-healing:** deleting an API Pod causes Kubernetes to recreate it.
- **Scaling:** the API was scaled from 3 to 5 replicas.
- **Rolling update:** API version `v1` was updated to `v2` without taking the deployment offline.
- **Rollback:** the deployment was successfully reverted from `v2` to `v1`.
- **Service discovery:** the `bank-api` Service dynamically tracked the API Pod endpoints.
- **Ingress routing:** external HTTP traffic was routed through NGINX Ingress → Service → Pods.
- **Persistent storage:** PostgreSQL uses a 1 GiB PersistentVolumeClaim.
- **Observability:** Pods, Services, ReplicaSets, Deployments, endpoints, rollout history, and Kubernetes events were inspected during operation.

---

## Infrastructure as Code

The `terraform/` directory contains the project's AWS infrastructure configuration, including networking and security resources.

Terraform configuration was validated locally with:

```bash
terraform init
terraform validate
```

The AWS infrastructure has **not been applied** in this environment; the configuration is included as Infrastructure as Code for the project's cloud architecture.

---

## What This Project Demonstrates

This project represents the progression from a backend application to a cloud-native deployment workflow:

```text
Python / Flask
      ↓
PostgreSQL
      ↓
Automated Tests
      ↓
Docker
      ↓
GitHub Actions
      ↓
GHCR
      ↓
Kubernetes
      ↓
NGINX Ingress
      ↓
Scaling + Self-Healing
      ↓
Rolling Updates + Rollbacks
```

The main focus is not simply building an API, but understanding how an application is **tested, packaged, shipped, deployed, exposed, scaled, and operated**.

---

## Author

**Roen Ominde**

GitHub: https://github.com/ominderoen2-cloud
