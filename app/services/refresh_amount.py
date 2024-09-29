from sqlalchemy.orm import Session
from models.product import Product


def refresh_amount(ordered_amount: int, product_id: int, db: Session) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    product.amount -= ordered_amount
    db.commit()
    db.refresh(product)
    return product
    