# Product Management System

This is a simple Product Management System built with FastAPI, SQLAlchemy, Alembic, and Pydantic. It provides a RESTful API for managing products, including CRUD operations, inventory tracking, and category classification.

## Features

- **CRUD operations** for products.
- **Inventory Management:** Track product quantities.
- **Category Classification:** Products can be assigned to categories.
- **Data Validation:** Ensures product data integrity using Pydantic.
- **Database Migrations:** Handled with Alembic.

## Technologies Used

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- PostgreSQL (database)
- Docker (for running the server)

---

## Table of Contents

1. [Installation](#installation-and-running)
6. [Contributing](#contributing)

---

## Installation-and-running

   ```bash
   git clone https://github.com/Narberal90/product-management-system.git
   cd product-management-system
   docker-compose up --build
   ```


The API will be available at `http://127.0.0.1:8000/docs`

## CURL Commands

### Create Category
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/categories/" -H "Content-Type: application/json" -d '{
    "name": "Fruits"
}'
```

### Get Category
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/categories/1"
```

### Create Product
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/products/" -H "Content-Type: application/json" -d '{
    "name": "Apple",
    "description": "Test apple",
    "price": 10.5,
    "quantity": 5,
    "category_id": 1
}'
```

### Update Product
```bash
curl -X PUT "http://127.0.0.1:8000/api/v1/products/1" -H "Content-Type: application/json" -d '{
    "name": "Updated Product Name",
    "price": 15.5
}'
```

### Delete Product
```bash
curl -X DELETE "http://127.0.0.1:8000/api/v1/products/1"
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature (`git switch -c feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.
