from fastapi import FastAPI, HTTPException
from database import Base, engine, SessionLocal
from models.customer import Customer
from services.ingestion import ingest_data

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/api/ingest")
def ingest():
    count=ingest_data()
    return {"status": "success", "records_processed": count}

@app.get("/api/customers")
def get_customers(page: int = 1, limit: int = 10):
    db=SessionLocal()

    start=(page-1)*limit

    data=db.query(Customer).offset(start).limit(limit).all()

    return data

@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str):
    db=SessionLocal()

    customer=db.query(Customer).filter_by(customer_id=customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Not found")

    return customer