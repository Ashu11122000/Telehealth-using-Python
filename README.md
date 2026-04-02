# AI-Assisted Telehealth Backend System

## Overview

The Telehealth Backend System is a scalable, modular, and production-grade backend application designed for a digital healthcare platform.

It enables:

* Patient-doctor interaction
* Medical record management
* AI-assisted health insights

Built using modern Python technologies and clean architecture, the system is designed for scalability, security, and future extensibility (AI, GraphQL, microservices).

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### Authentication

* JWT (python-jose)
* Password hashing (passlib + bcrypt)

### DevOps

* Docker
* Docker Compose
* UV (modern package manager)

### Testing

* Pytest
* HTTPX

---

# System Architecture (HLD)

## High-Level Architecture Flow

```id="hld1"
Client (Postman / Frontend)
        ↓
API Layer (FastAPI)
        ↓
Middleware Layer (JWT, CORS, Logging)
        ↓
Service Layer (Business Logic)
        ↓
Repository Layer (Data Access)
        ↓
ORM Layer (SQLAlchemy)
        ↓
Database Layer (PostgreSQL)
```

---

## API Layer HLD

```id="hld2"
Client Request
      ↓
FastAPI Router
      ↓
Dependency Injection
      ↓
Middleware
      ↓
Request Validation (Pydantic)
      ↓
Service Layer
      ↓
Response Serialization
      ↓
Client Response
```

---

## Middleware Layer HLD

```id="hld3"
Request
  ↓
CORS Middleware
  ↓
Logging Middleware
  ↓
JWT Authentication
  ↓
RBAC Authorization
  ↓
Rate Limiting
  ↓
API Layer
```

---

## Service Layer HLD

```id="hld4"
API Layer
   ↓
Service Layer
   ├── User Service
   ├── Appointment Service
   ├── Medical Record Service
   └── AI Service
   ↓
Repository Layer
```

---

## Repository Layer HLD

```id="hld5"
Service Layer
      ↓
Repository Layer
      ↓
ORM Layer
```

---

## ORM Layer HLD

```id="hld6"
Repository Layer
      ↓
SQLAlchemy ORM
      ↓
Database
```

---

## Database Layer HLD

```id="hld7"
PostgreSQL Database

Tables:
- users
- doctor_profiles
- appointments
- medical_records
- ai_assessments
- symptoms
```

---

## Infrastructure Layer HLD

```id="hld8"
Docker Compose
   ├── FastAPI Container
   └── PostgreSQL Container
```

---

# Project Structure

```id="structure"
telehealth-backend/
│
├── app/                         
│
│   ├── main.py                   # FastAPI entry point
│   ├── __init__.py
│
│   ├── api/                     
│   │   ├── deps.py              
│   │   ├── v1/                 
│   │   │   ├── api.py           
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py
│   │   │   │   ├── users.py
│   │   │   │   ├── doctors.py
│   │   │   │   ├── appointments.py
│   │   │   │   ├── medical_records.py
│   │   │   │   ├── ai.py
│   │   │   │   └── health.py     # Health check
│
│   ├── core/                     
│   │   ├── config.py             # Settings 
│   │   ├── security.py           # JWT
│   │   ├── middleware/
│   │   │   ├── auth_middleware.py
│   │   │   ├── logging.py
│   │   │   └── rate_limit.py
│
│   ├── db/                       # Database
│   │   ├── base.py              
│   │   ├── session.py            # DB session
│   │   ├── init_db.py            # Initial 
│
│   ├── models/                  
│   │   ├── user.py
│   │   ├── doctor_profile.py
│   │   ├── appointment.py
│   │   ├── medical_record.py
│   │   ├── ai_assessment.py
│   │   ├── symptom.py
│   │   └── __init__.py
│
│   ├── schemas/                 
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── doctor.py
│   │   ├── appointment.py
│   │   ├── medical_record.py
│   │   ├── ai.py
│   │   └── __init__.py
│
│   ├── repositories/            
│   │   ├── user_repository.py
│   │   ├── doctor_repository.py
│   │   ├── appointment_repository.py
│   │   ├── medical_repository.py
│   │   ├── ai_repository.py
│   │   └── __init__.py
│
│   ├── services/                
│   │   ├── user_service.py
│   │   ├── auth_service.py
│   │   ├── doctor_service.py
│   │   ├── appointment_service.py
│   │   ├── medical_service.py
│   │   ├── ai_service.py
│   │   └── __init__.py
│
│   ├── utils/                   
│   │   ├── helpers.py
│   │   ├── constants.py
│   │   └── exceptions.py
│
│   ├── tests/                    # Unit Tests
│   │   ├── test_auth.py
│   │   ├── test_users.py
│   │   ├── test_appointments.py
│   │   └── __init__.py
│
├── alembic/                      
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│
├── alembic.ini
│
├── .env                          
├── .env.example                  # Sample env
│
├── docker-compose.yml            # Docker setup
├── Dockerfile                    # App container
│
├── pyproject.toml              
├── README.md

```

---

