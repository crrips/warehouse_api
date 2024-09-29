from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.product import Product
from models.order import Order, OrderStatus
from models.order import OrderStatus
from models.orderItem import OrderItem
from db import get_db
import time
from services.check_availability import check_availability
from services.refresh_amount import refresh_amount


router = APIRouter()


@router.post("/products")
def create_product(name: str, description: str, price: float, amount: int, db: Session = Depends(get_db)):
    product = Product(name=name, description=description, price=price, amount=amount)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@router.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    return product


@router.put("/products/{id}")
def update_product(id: int, name: str, description: str, price: float, amount: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    product.name = name
    product.description = description
    product.price = price
    product.amount = amount
    db.commit()
    db.refresh(product)
    return product


@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    name = product.name
    db.delete(product)
    db.commit()
    return {"message": f"Product {name} has been deleted successfully"}


@router.post("/orders")
def create_order(order_id: int, product_id: int, product_amount: int, db: Session = Depends(get_db)):
    cur_amount = db.query(Product).filter(Product.id == product_id).first().amount
    
    try:
        check_availability(cur_amount=cur_amount, ordered_amount=product_amount)
    except ValueError as e:
        return {"message": str(e)}
    
    date_created = time.asctime()
    status = OrderStatus.IN_PROCESS.value
    order = Order(date_created=date_created, status=status)
    db.add(order)
    db.commit()
    db.refresh(order)
    
    orderItem = OrderItem(order_id=order_id, product_id=product_id, product_amount=product_amount)
    db.add(orderItem)
    db.commit()
    db.refresh(orderItem)
    refresh_amount(ordered_amount=product_amount, product_id=product_id, db=db)
    
    return order


@router.get("/orders")
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders
    

@router.get("/orders/{id}")
def get_order_by_id(id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == id).first()
    return order


@router.patch("/orders/{id}/status")
def update_order_status(id: int, status: OrderStatus, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == id).first()
    order.status = status.value
    db.commit()
    db.refresh(order)
    return order



@router.get("/")
def read_root():
    return {"message": "Welcome to the Warehouse API"}


def get_router() -> APIRouter:
    return router
