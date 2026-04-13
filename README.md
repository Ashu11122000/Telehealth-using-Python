# AI-Assisted Telehealth Backend System

---

## Overview

The Telehealth Backend System is a scalable, modular backend application designed to support a digital healthcare platform
where patients can interact with doctors, manage medical records, and receive basic AI-assisted health insights.
This project focuses on building a production-style backend architecture using modern technologies such as:

- FastAPI (high-performance APIs)
- PostgreSQL (relational database)
- SQLAlchemy (ORM)
- Pydantic (data validation)
- Docker (containerization)

The system is designed with clean architecture principles, enabling future integration of advanced features such as AI models, GraphQL APIs, and microservices.

---

## Objectives

- Build a robust (strong) backend system for telehealth workflows
- Design a well-structured relational database
- Implement secure authentication and authorization
- Develop scalable REST APIs
- Ensure data validation and integrity
- Prepare the system for future AI integration

---

## Core Features

- **Authentication & Security**
  - User registration and login
  - Password hashing (secure storage)
  - JWT-based authentication
  - Role-based access control (RBAC)
  - Environment-based configuration using .env

- **User Management**
  - Patient and Doctor roles
  - Profile management
  - Role-based permissions

- **Appointment Management**
  - Book appointments
  - Cancel appointments
  - Check doctor availability
  - Prevent double booking (data integrity)

- **Medical Records**
  - Store patient health records
  - Maintain medical history
  - Link records with users

- **Basic AI Symptom Module (Rule-Based)**
  - Accept symptom inputs
  - Perform simple rule-based analysis
  - Classify risk levels (Low / Medium / High)
  - Provide basic health suggestions

- **API Infrastructure**
  - RESTful API design
  - CORS configuration for frontend integration
  - Structured request/response validation

- **Testing**
  - Unit tests for critical modules
  - API validation and error handling

- **Containerization**
  - Dockerized backend service
  - Docker Compose for running:
  - FastAPI server
  - PostgreSQL database

---

## Technology Stack

- **Backend**
  - Python
  - FastAPI
  - Pydantic
  - SQLAlchemy

- **Database**
  - PostgreSQL

- **Configuration**
  - Dotenv (.env)

- **Testing**
  - Pytest / Unit Testing

- **API Features**
  - REST APIs
  - CORS support

- **DevOps**
  - Docker
  - Docker Compose

---

## Conclusion

- This project demonstrates the development of a real-world backend system for a telehealth platform using modern Python technologies.
- It emphasizes scalability, security, and clean architecture, making it a strong foundation for building advanced healthcare applications.

---

## Main Flow of Application

┌────────────────────────────────────────────────────────────┐
│ Client Layer │
│ (Postman / Future Next.js Frontend) │
└───────────────────────────┬────────────────────────────────┘
│ HTTP Request (JSON)
▼
┌────────────────────────────────────────────────────────────┐
│ API Layer (FastAPI) │
│------------------------------------------------------------│
│ - Route Handling (/auth, /users, /appointments) │
│ - Request/Response Models (Pydantic) │
│ - Input Validation │
└───────────────────────────┬────────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────┐
│ Middleware Layer (Core) │
│------------------------------------------------------------│
│ - JWT Authentication │
│ - CORS Handling │
│ - Logging (optional) │
│ - Error Handling │
└───────────────────────────┬────────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────┐
│ Service Layer (Business Logic) │
│------------------------------------------------------------│
│ - User Service │
│ - Appointment Service │
│ - Medical Record Service │
│ - AI Symptom Service (Rule-based) │
└───────────────────────────┬────────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────┐
│ Repository Layer (Data Access) │
│------------------------------------------------------------│
│ - DB Queries │
│ - CRUD Operations │
│ - Abstraction over ORM │
└───────────────────────────┬────────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────┐
│ ORM Layer (SQLAlchemy) │
│------------------------------------------------------------│
│ - Model Mapping (Python ↔ Tables) │
│ - Session Management │
│ - Transactions │
└───────────────────────────┬────────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────┐
│ Database Layer (PostgreSQL) │
│------------------------------------------------------------│
│ - Users │
│ - Doctors │
│ - Appointments │
│ - Medical Records │
└────────────────────────────────────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────┐
│ Infrastructure Layer (Docker) │
│ - FastAPI Container │
│ - PostgreSQL Container │
└────────────────────────────────────────────────────────────┘

---

## API Layer HLD Architectural Layer

    Client Request (Postman / Frontend)
                       │
                       ▼

┌──────────────────────────────────────────────┐
│ FastAPI Router Layer │
│----------------------------------------------│
│ - Endpoint mapping (/auth, /appointments) │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Dependency Injection Layer │
│----------------------------------------------│
│ - DB Session (Depends) │
│ - Current User (JWT) │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Middleware Layer (Pre-processing) │
│----------------------------------------------│
│ - JWT Validation │
│ - CORS Handling │
│ - Logging │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Request Validation (Pydantic) │
│----------------------------------------------│
│ - Input schema validation │
│ - Data parsing │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Service Layer Call (Business Logic) │
│----------------------------------------------│
│ - Calls appropriate service │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Response Serialization (Pydantic) │
│----------------------------------------------│
│ - Output schema │
│ - JSON response formatting │
└──────────────────────┬───────────────────────┘
│
▼
Client Response (JSON)

---

## Middleware HLD architectural flow diagram

             Client Request (HTTP)
                      │
                      ▼

┌──────────────────────────────────────────────┐
│ CORS Middleware │
│----------------------------------------------│
│ - Checks allowed origins │
│ - Handles preflight (OPTIONS) requests │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Logging Middleware │
│----------------------------------------------│
│ - Logs request (method, URL, time) │
│ - Tracks performance │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Authentication Middleware (JWT) │
│----------------------------------------------│
│ - Extract token from header │
│ - Validate JWT │
│ - Decode user info │
│ - Attach user to request context │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Authorization Check (RBAC) │
│----------------------------------------------│
│ - Verify role (Patient/Doctor/Admin) │
│ - Allow / Deny access │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Rate Limiting (Optional) │
│----------------------------------------------│
│ - Prevent abuse / DDoS │
│ - Limit requests per user/IP │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Request Passed to API Layer │
└──────────────────────────────────────────────┘

---

## Service Layer HLD architectural flow diagram

                Request from API Layer
                         │
                         ▼

┌──────────────────────────────────────────────┐
│ Service Layer (Business Logic) │
│----------------------------------------------│
│ │
│ ┌───────────────┐ ┌───────────────────┐ │
│ │ User Service │ │ Appointment │ │
│ │ │ │ Service │ │
│ │ - Register │ │ - Book │ │
│ │ - Login │ │ - Cancel │ │
│ │ - RBAC │ │ - Availability │ │
│ └──────┬────────┘ └─────────┬─────────┘ │
│ │ │ │
│ ▼ ▼ │
│ ┌───────────────┐ ┌───────────────────┐ │
│ │ Medical │ │ AI Symptom │ │
│ │ Record Service│ │ Service │ │
│ │ - Store │ │ - Risk Analysis │ │
│ │ - History │ │ - Rule Engine │ │
│ └──────┬────────┘ └─────────┬─────────┘ │
│ │ │ │
│ └──────────────┬───────┘ │
│ ▼ │
│ Repository Layer (DB Access) │
└──────────────────────────────────────────────┘

---

## Repository HLD architecture flow diagram

               Service Layer
                     │
                     ▼

┌──────────────────────────────────────────────┐
│ Repository Layer │
│----------------------------------------------│
│ - UserRepository │
│ - AppointmentRepository │
│ - MedicalRecordRepository │
│----------------------------------------------│
│ Responsibilities: │
│ - CRUD operations │
│ - Query abstraction │
│ - No business logic │
└──────────────────────┬───────────────────────┘
│
▼
ORM Layer (SQLAlchemy)

---

## ORM Layer HLD architectural flow diagram

               Repository Layer
                      │
                      ▼

┌──────────────────────────────────────────────┐
│ ORM Layer (SQLAlchemy) │
│----------------------------------------------│
│ - Model Mapping (Python ↔ Tables) │
│ - Session Management │
│ - Query Translation │
│----------------------------------------------│
│ Example: │
│ User → users table │
└──────────────────────┬───────────────────────┘
│
▼
Database Layer (PostgreSQL)

---

## Database Layer HLD architectural Flow Diagram

                  ORM Layer
                     │
                     ▼

┌──────────────────────────────────────────────┐
│ Database Layer (PostgreSQL) │
│----------------------------------------------│
│ Tables: │
│ - users │
│ - doctors │
│ - appointments │
│ - medical_records │
│----------------------------------------------│
│ Features: │
│ - ACID transactions │
│ - Indexing │
│ - Constraints (FK, PK) │
└──────────────────────────────────────────────┘

---

## Infrastructure Layer HLD architectural flow diagram

┌──────────────────────────────────────────────┐
│ Infrastructure Layer │
│----------------------------------------------│
│ Docker Compose │
│----------------------------------------------│
│ ┌────────────────────┐ ┌────────────────┐ │
│ │ FastAPI Container │ │ PostgreSQL DB │ │
│ │--------------------│ │----------------│ │
│ │ - API Server │ │ - Data Storage │ │
│ │ - Business Logic │ │ - Tables │ │
│ └─────────┬──────────┘ └────────┬───────┘ │
│ │ │ │
│ └────── Network ────────┘ │
└──────────────────────────────────────────────┘

---

## ERD Diagram

          ┌──────────────┐
          │    users     │
          │--------------│
          │ id (PK)      │
          │ email        │
          │ password     │
          │ role         │
          └──────┬───────┘
                 │
     ┌───────────┴────────────┐
     ▼                        ▼

┌──────────────┐ ┌──────────────────┐
│doctor_profile│ │ medical_records │
│--------------│ │------------------│
│ id (PK) │ │ id (PK) │
│ user_id (FK) │ │ user_id (FK) │
│specialization│ │ title │
│ experience │ │ description │
└──────┬───────┘ └──────┬───────────┘
│ │
▼ ▼

      ┌────────────────────────────┐
      │       appointments         │
      │----------------------------│
      │ id (PK)                    │
      │ patient_id (FK → users)    │
      │ doctor_id (FK → users)     │
      │ date_time                  │
      │ status                     │
      └──────────┬─────────────────┘
                 │
                 ▼

      ┌────────────────────────────┐
      │      ai_assessments        │
      │----------------------------│
      │ id (PK)                    │
      │ user_id (FK)               │
      │ risk_level                 │
      │ summary                    │
      └──────────┬─────────────────┘
                 │
                 ▼

      ┌────────────────────────────┐
      │         symptoms           │
      │----------------------------│
      │ id (PK)                    │
      │ assessment_id (FK)         │
      │ name                       │
      │ severity                   │
      └────────────────────────────┘

---

## Backend Folder Structure

telehealth-backend/
│
├── app/ # Main application package
│
│ ├── main.py # FastAPI entry point
│ ├── **init**.py
│
│ ├── api/ # API Layer (Routing)
│ │ ├── deps.py # Dependencies (JWT, DB session)
│ │ ├── v1/ # Versioning (best practice)
│ │ │ ├── api.py # Combine all routes
│ │ │ ├── endpoints/
│ │ │ │ ├── auth.py
│ │ │ │ ├── users.py
│ │ │ │ ├── doctors.py
│ │ │ │ ├── appointments.py
│ │ │ │ ├── medical_records.py
│ │ │ │ ├── ai.py
│ │ │ │ └── health.py # Health check
│
│ ├── core/ # Core configs & middleware
│ │ ├── config.py # Settings (.env loader)
│ │ ├── security.py # JWT, password hashing
│ │ ├── middleware/
│ │ │ ├── auth_middleware.py
│ │ │ ├── logging.py
│ │ │ └── rate_limit.py
│
│ ├── db/ # Database setup
│ │ ├── base.py # Base class for models
│ │ ├── session.py # DB session
│ │ ├── init_db.py # Initial data (optional)
│
│ ├── models/ # ORM Models (SQLAlchemy)
│ │ ├── user.py
│ │ ├── doctor_profile.py
│ │ ├── appointment.py
│ │ ├── medical_record.py
│ │ ├── ai_assessment.py
│ │ ├── symptom.py
│ │ └── **init**.py
│
│ ├── schemas/ # Pydantic Schemas
│ │ ├── user.py
│ │ ├── auth.py
│ │ ├── doctor.py
│ │ ├── appointment.py
│ │ ├── medical_record.py
│ │ ├── ai.py
│ │ └── **init**.py
│
│ ├── repositories/ # Data Access Layer
│ │ ├── user_repository.py
│ │ ├── doctor_repository.py
│ │ ├── appointment_repository.py
│ │ ├── medical_repository.py
│ │ ├── ai_repository.py
│ │ └── **init**.py
│
│ ├── services/ # Business Logic Layer
│ │ ├── user_service.py
│ │ ├── auth_service.py
│ │ ├── doctor_service.py
│ │ ├── appointment_service.py
│ │ ├── medical_service.py
│ │ ├── ai_service.py
│ │ └── **init**.py
│
│ ├── utils/ # Utility functions
│ │ ├── helpers.py
│ │ ├── constants.py
│ │ └── exceptions.py
│
│ ├── tests/ # Unit Tests
│ │ ├── test_auth.py
│ │ ├── test_users.py
│ │ ├── test_appointments.py
│ │ └── **init**.py
│
├── documentations/ # Project Documentation (NEW)
│ ├── CORS.md
│ ├── Dotenv.md
│ ├── FastAPI.md
│ ├── Pydantic.md
│ ├── Python.md
│ ├── SQLAlchemy.md
│ ├── Unit_Test.md
│ ├── UV.md
│ └── Virtual_Environment.md
│
├── alembic/ # DB migrations
│ ├── versions/
│ ├── env.py
│ ├── script.py.mako
│
├── alembic.ini
│
├── .env # Environment variables
├── .env.example # Sample env
│
├── docker-compose.yml # Docker setup
├── Dockerfile # App container
│
├── pyproject.toml # Dependencies (uv)
├── README.md

---

## PHASE 1 — Core Configuration (VERY IMPORTANT)

---

## Goal

Make your app run properly and be configurable.

---

## What You Build

Work inside the following directories:
`app/core/`
`app/db/`

---

## Tasks

### 1. Environment Variables & Configuration

- Setup `.env`
- Configure:
  - Database URL
  - Secret Key
  - JWT settings

**File:**

`app/core/config.py`

---

### 2. Database Connection

- Create SQLAlchemy engine
- Setup `SessionLocal`
- Define `Base` class

**Files:**

`db/session.py`
`db/base.py`

---

### 3. Application Entry Point

- Create FastAPI app
- Add CORS middleware
- Include routers (later)

**File:**

`app/main.py`

- Create FastAPI app
- Add CORS
- Include routers (later)

---

## Output of Phase 1

- App runs successfully
- Database connection works
- Configuration is properly managed
