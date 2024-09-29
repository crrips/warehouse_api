# Warehouse Management API

## Description
This project is a Warehouse Management API built using FastAPI, SQLAlchemy, and PostgreSQL. It allows for managing products, orders, and order items with the ability to perform various CRUD operations and manage inventory.

## Usage
```bash
./run_api.sh
```

## Database Structure
Product: Represents items available in the warehouse.
Fields: id, name, description, price, amount.

Order: Represents orders made by customers.
Fields: id, date_created, status (e.g., "in progress", "sent", "delivered").

OrderItem: Represents items within an order.
Fields: id, order_id, product_id, product_amount.

## Endpoints
### Products
```
Create Product: POST /products - Create a new product.

Get Products: GET /products - Retrieve a list of all products.

Get Product by ID: GET /products/{id} - Retrieve details of a specific product.

Update Product: PUT /products/{id} - Update product details.

Delete Product: DELETE /products/{id} - Delete a product.
```
### Orders
```
Create Order: POST /orders - Create a new order.

Get Orders: GET /orders - Retrieve a list of all orders.

Get Order by ID: GET /orders/{id} - Retrieve details of a specific order.

Update Order Status: PATCH /orders/{id}/status - Update the status of an order.
```
## Services
Stock Verification: When creating an order, it ensures there is sufficient product stock.

Stock Update: Reducing product stock when an order is created.

Error Handling: If there is insufficient stock for an order, return an appropriate error message.
