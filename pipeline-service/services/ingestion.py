import requests
from database import SessionLocal
from models.customer import Customer

FLASK_URL="http://mock-server:5000/api/customers"

def ingest_data():
    db=SessionLocal()

    page=1
    limit=10
    total_processed=0

    while True:
        res=requests.get(f"{FLASK_URL}?page={page}&limit={limit}")
        data=res.json()

        customers=data["data"]

        if not customers:
            break

        for c in customers:
            existing=db.query(Customer).filter_by(customer_id=c["customer_id"]).first()

            if existing:
                for key, value in c.items():
                    setattr(existing, key, value)
            else:
                db.add(Customer(**c))

            total_processed+=1

        db.commit()
        page+=1

    return total_processed