# Banking API

[svg](https://github.com/ominderoen2-cloud/bank#banking-api)

A production-oriented RESTful banking API built with **Python, Flask, and PostgreSQL**. The project started as a layered backend application and evolved into a containerized, CI/CD-enabled Kubernetes deployment.

It demonstrates backend engineering and cloud-native fundamentals including layered architecture, automated testing, Docker, GitHub Actions, GitHub Container Registry, Kubernetes, NGINX Ingress, configuration management, secrets, persistent storage, scaling, self-healing, rolling deployments, and rollbacks.

---

## Architecture

[svg](https://github.com/ominderoen2-cloud/bank#architecture)

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
             └────────── API replicas ───┘
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

[svg](https://github.com/ominderoen2-cloud/bank#features)

### Banking API

[svg](https://github.com/ominderoen2-cloud/bank#banking-api-1)

* User registration and login
* Fixed account management
* Junior account management
* Premium account management
* Transaction management
* Input validation
* PostgreSQL persistence
* Layered architecture: **Routes → Services → Repositories**
* Automated tests with Pytest

### Cloud & DevOps

[svg](https://github.com/ominderoen2-cloud/bank#cloud--devops)

* Docker containerization
* Docker Compose for local multi-container development
* GitHub Actions CI/CD
* Automated Pytest execution
* Docker image publishing to GitHub Container Registry (GHCR)
* Commit-SHA image tagging for traceable deployments
* Kubernetes deployment with Kind
* Kubernetes ConfigMaps and Secrets
* Kubernetes Service discovery
* NGINX Ingress routing
* Persistent PostgreSQL storage using a PVC
* Kubernetes self-healing
* Kubernetes scaling
* Rolling updates
* Deployment rollbacks
* Kubernetes resource and event inspection

---

## Tech Stack

[svg](https://github.com/ominderoen2-cloud/bank#tech-stack)

| Technology                | Purpose                  |
| ------------------------- | ------------------------ |
| Python                    | Backend language         |
| Flask                     | REST API framework       |
| PostgreSQL                | Relational database      |
| Psycopg2                  | PostgreSQL driver        |
| Pytest                    | Automated testing        |
| Docker                    | Containerization         |
| Docker Compose            | Local orchestration      |
| GitHub Actions            | CI/CD                    |
| GitHub Container Registry | Container image registry |
| Kubernetes                | Container orchestration  |
| Kind                      | Local Kubernetes cluster |
| NGINX Ingress             | HTTP routing             |
| Terraform                 | Infrastructure as Code   |
| Git & GitHub              | Version control          |

---

## Project Structure

[svg](https://github.com/ominderoen2-cloud/bank#project-structure)

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

[svg](https://github.com/ominderoen2-cloud/bank#api-endpoints)

### Health

[svg](https://github.com/ominderoen2-cloud/bank#health)

| Method | Endpoint  | Description  |
| ------ | --------- | ------------ |
| GET    | `/`       | API status   |
| GET    | `/health` | Health check |

### Authentication

[svg](https://github.com/ominderoen2-cloud/bank#authentication)

| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| POST   | `/register` | Register a user     |
| POST   | `/login`    | Authenticate a user |

### Fixed Accounts

[svg](https://github.com/ominderoen2-cloud/bank#fixed-accounts)

| Method | Endpoint                                 | Description                   |
| ------ | ---------------------------------------- | ----------------------------- |
| POST   | `/fixed`                                 | Create account                |
| GET    | `/fixed`                                 | List accounts                 |
| GET    | `/fixed/account_number/<account_number>` | Get account by account number |
| GET    | `/fixed/id/<national_id>`                | Get account by national ID    |
| PUT    | `/fixed/<account_number>`                | Update account                |
| DELETE | `/fixed/<account_number>`                | Delete account                |

### Junior Accounts

[svg](https://github.com/ominderoen2-cloud/bank#junior-accounts)

| Method | Endpoint                                               | Description                      |
| ------ | ------------------------------------------------------ | -------------------------------- |
| POST   | `/junior`                                              | Create account                   |
| GET    | `/junior`                                              | List accounts                    |
| GET    | `/junior/account_number/<account_number>`              | Get account                      |
| GET    | `/junior/birth_certificate/<birth_certificate_number>` | Get account by birth certificate |
| PUT    | `/junior/<account_number>`                             | Update account                   |
| DELETE | `/junior/<account_number>`                             | Delete account                   |

### Premium Accounts

[svg](https://github.com/ominderoen2-cloud/bank#premium-accounts)

| Method | Endpoint                                   | Description                |
| ------ | ------------------------------------------ | -------------------------- |
| POST   | `/premium`                                 | Create account             |
| GET    | `/premium`                                 | List accounts              |
| GET    | `/premium/account_number/<account_number>` | Get account                |
| GET    | `/premium/national_id/<national_id>`       | Get account by national ID |
| PUT    | `/premium/<account_number>`                | Update account             |
| DELETE | `/premium/<account_number>`                | Delete account             |

### Transactions

[svg](https://github.com/ominderoen2-cloud/bank#transactions)

| Method | Endpoint                           | Description         |
| ------ | ---------------------------------- | ------------------- |
| POST   | `/trans`                           | Create transaction  |
| GET    | `/trans`                           | List transactions   |
| GET    | `/trans/trans_id/<transaction_id>` | Get transaction     |
| PUT    | `/trans/send/<transaction_id>`     | Send transaction    |
| PUT    | `/trans/recieve/<transaction_id>`  | Receive transaction |

---

## Local Development

[svg](https://github.com/ominderoen2-cloud/bank#local-development)

### 1. Clone the repository

[svg](https://github.com/ominderoen2-cloud/bank#1-clone-the-repository)

```bash
git clone https://github.com/ominderoen2-cloud/bank.git
cd bank
```

### 2. Create a virtual environment

[svg](https://github.com/ominderoen2-cloud/bank#2-create-a-virtual-environment)

#### Windows

[svg](https://github.com/ominderoen2-cloud/bank#windows)

```powershell
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

[svg](https://github.com/ominderoen2-cloud/bank#linuxmacos)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

[svg](https://github.com/ominderoen2-cloud/bank#3-install-dependencies)

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

[svg](https://github.com/ominderoen2-cloud/bank#4-configure-postgresql)

The application reads its database configuration from environment variables.

Example:

```text
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/bank
```

Do not commit real credentials or secrets to the repository.

### 5. Run the API

[svg](https://github.com/ominderoen2-cloud/bank#5-run-the-api)

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## Docker

[svg](https://github.com/ominderoen2-cloud/bank#docker)

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

[svg](https://github.com/ominderoen2-cloud/bank#testing)

Run the complete test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Current test status:

* **36 tests passing**
* **0 warnings**

The tests cover CRUD operations, validation, API behavior, and database interactions.

---

## CI/CD

[svg](https://github.com/ominderoen2-cloud/bank#cicd)

GitHub Actions automatically runs the pipeline on:

* Pushes to the `main` branch
* Pull requests targeting the `main` branch

The pipeline runs in a clean Ubuntu environment with PostgreSQL 16 and Python 3.14.

### Pull Requests

For pull requests, the pipeline:

1. Starts a PostgreSQL 16 service.
2. Checks out the repository.
3. Sets up Python 3.14.
4. Installs dependencies.
5. Runs Pytest.
6. Builds the Docker image.

Docker images are **not published** from pull requests.

### Pushes to `main`

For pushes to `main`, the pipeline:

1. Starts a PostgreSQL 16 service.
2. Checks out the repository.
3. Sets up Python 3.14.
4. Installs dependencies.
5. Runs Pytest.
6. Builds the Docker image.
7. Tags the image using the Git commit SHA.
8. Authenticates with GitHub Container Registry.
9. Publishes the image to GHCR.

This creates a reproducible path from a code change to a tested, versioned container image.

The current CI pipeline has been successfully verified on the `main` branch.

---

## Kubernetes

[svg](https://github.com/ominderoen2-cloud/bank#kubernetes)

The application can be deployed to a local Kubernetes cluster using **Kind**.

The Kubernetes configuration is located in `K8s/` and includes:

* Deployment
* Service
* NGINX Ingress
* ConfigMap
* Secret
* PostgreSQL Deployment
* PostgreSQL Service
* PersistentVolumeClaim

### Create the cluster

[svg](https://github.com/ominderoen2-cloud/bank#create-the-cluster)

```bash
kind create cluster --name bank
```

### Install the NGINX Ingress Controller

[svg](https://github.com/ominderoen2-cloud/bank#install-the-nginx-ingress-controller)

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

### Apply the Kubernetes resources

[svg](https://github.com/ominderoen2-cloud/bank#apply-the-kubernetes-resources)

```bash
kubectl apply -f K8s/
```

### Inspect the deployment

[svg](https://github.com/ominderoen2-cloud/bank#inspect-the-deployment)

```bash
kubectl get pods
kubectl get svc
kubectl get deployment
kubectl get ingress
```

### Scale the API

[svg](https://github.com/ominderoen2-cloud/bank#scale-the-api)

```bash
kubectl scale deployment bank-api --replicas=5
```

### Monitor a rollout

[svg](https://github.com/ominderoen2-cloud/bank#monitor-a-rollout)

```bash
kubectl rollout status deployment bank-api
```

### View rollout history

[svg](https://github.com/ominderoen2-cloud/bank#view-rollout-history)

```bash
kubectl rollout history deployment bank-api
```

### Roll back a deployment

[svg](https://github.com/ominderoen2-cloud/bank#roll-back-a-deployment)

```bash
kubectl rollout undo deployment bank-api
```

### Inspect cluster events

[svg](https://github.com/ominderoen2-cloud/bank#inspect-cluster-events)

```bash
kubectl get events --sort-by=.lastTimestamp
```

### Access the API through the Ingress

[svg](https://github.com/ominderoen2-cloud/bank#access-the-api-through-the-ingress)

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

[svg](https://github.com/ominderoen2-cloud/bank#kubernetes-capabilities-demonstrated)

This project was used to demonstrate real Kubernetes operational behavior rather than only writing manifests:

* **Self-healing:** deleting an API Pod causes Kubernetes to recreate it.
* **Scaling:** the API has been demonstrated scaling from 3 to 5 replicas.
* **Rolling update:** API version `v1` was updated to `v2` without taking the deployment offline.
* **Rollback:** the deployment was successfully reverted from `v2` to `v1`.
* **Service discovery:** the `bank-api` Service dynamically tracked the API Pod endpoints.
* **Ingress routing:** external HTTP traffic was routed through NGINX Ingress → Service → Pods.
* **Persistent storage:** PostgreSQL uses a 1 GiB PersistentVolumeClaim.
* **Observability:** Pods, Services, ReplicaSets, Deployments, endpoints, rollout history, and Kubernetes events were inspected during operation.

---

## Infrastructure as Code

[svg](https://github.com/ominderoen2-cloud/bank#infrastructure-as-code)

The `terraform/` directory contains the project's AWS infrastructure configuration, including networking and security resources.

Terraform configuration was validated locally with:

```bash
terraform init
terraform validate
```

The AWS infrastructure has **not been applied** in this environment; the configuration is included as Infrastructure as Code for the project's cloud architecture.

---

## What This Project Demonstrates

[svg](https://github.com/ominderoen2-cloud/bank#what-this-project-demonstrates)

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

[svg](https://github.com/ominderoen2-cloud/bank#author)

**Roen Ominde**

GitHub: https://github.com/ominderoen2-cloud
