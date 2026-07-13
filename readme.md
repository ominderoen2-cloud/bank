#  Banking API

A RESTful Banking API built with **Flask** and **PostgreSQL** following a layered architecture (Routes → Services → Repositories). The project supports creating and managing different bank account types while demonstrating backend best practices such as validation, testing, and separation of concerns.

---

##  Features

- Create, update, retrieve, and delete:
  - Fixed Accounts
  - Junior Accounts
  - Transactions
- Input validation
- PostgreSQL database
- Layered architecture
- Automated tests with Pytest

---

##  Tech Stack

- Python 3
- Flask
- PostgreSQL
- Psycopg2
- Pytest
- Git & GitHub

---

##  Project Structure

```
bank/
│
├── repositories/
├── routes/
├── services/
├── validators/
├── tests/
├── app.py
├── connect_db.py
└── requirements.txt
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/ominderoen2-cloud/bank.git

cd bank
```

### Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create a PostgreSQL database and update the connection settings inside:

```
connect_db.py
```

with your PostgreSQL credentials.

Example:

```python
database="bank"
user="postgres"
password="your_password"
host="localhost"
port="5432"
```

---

##  Running the API

```bash
python app.py
```

The server starts on

```
http://127.0.0.1:5000
```

---

##  Running Tests

Run every test

```bash
pytest
```

Run with verbose output

```bash
pytest -v
```

Current status:

-  26 tests passing

---

##  API Endpoints

### Fixed Accounts

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /fixed | Create account |
| GET | /fixed | List accounts |
| GET | /fixed/<account_number> | Get account |
| PUT | /fixed/<account_number> | Update account |
| DELETE | /fixed/<account_number> | Delete account |

---

### Junior Accounts

| Method | Endpoint |
|---------|----------|
| POST | /junior |
| GET | /junior |
| GET | /junior/account_number/<account_number> |
| GET | /junior/birth_certificate/<birth_certificate_number> |
| PUT | /junior/<account_number> |
| DELETE | /junior/<account_number> |

---

### Transactions

| Method | Endpoint |
|---------|----------|
| POST | /trans |
| GET | /trans |
| GET | /trans/trans_id/<transaction_id> |
| PUT | /trans/send/<transaction_id> |
| PUT | /trans/recieve/<transaction_id> |

---

##  Testing

This project includes automated unit tests using **Pytest** to verify:

- CRUD operations
- Validation
- API responses
- Database interactions

---

##  Future Improvements

- JWT Authentication
- Docker support
- CI/CD with GitHub Actions
- API documentation (Swagger/OpenAPI)
- AWS deployment
- Terraform infrastructure

---

##  Author

**Roen Ominde**

GitHub:
https://github.com/ominderoen2-cloud