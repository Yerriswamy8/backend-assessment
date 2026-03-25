from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_data():
    with open("data/customers.json") as f:
        return json.load(f)

@app.route("/api/health")
def health():
    return {"status": "ok"}

@app.route("/api/customers")
def get_customers():
    data = load_data()

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": data[start:end],
        "total": len(data),
        "page": page,
        "limit": limit
    })

@app.route("/api/customers/<customer_id>")
def get_customer(customer_id):
    data = load_data()
    for c in data:
        if c["customer_id"] == customer_id:
            return c
    return {"error": "Customer not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)