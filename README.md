# Backend Assessment

## Architecture
Flask → FastAPI → PostgreSQL

## Run
docker-compose up -d

## APIs

### Flask
- GET /api/customers
- GET /api/customers/{id}

### FastAPI
- POST /api/ingest
- GET /api/customers
- GET /api/customers/{id}

## How to Test

1. Start services:
   docker-compose up --build -d

2. Test Flask:
   http://localhost:5000/api/customers

3. Ingest data:
   POST http://localhost:8000/api/ingest

4. Verify data:
   http://localhost:8000/api/customers