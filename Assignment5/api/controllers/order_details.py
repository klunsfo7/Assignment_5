from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models

def create(db: Session, order_detail):
    # Create a new instance of the OrderDetail model with the provided data
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        quantity=order_detail.quantity
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update(db: Session, order_detail_id, order_detail):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    update_data = order_detail.model_dump(exclude_unset=True)
    db_order_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_detail.first()

def delete(db: Session, order_detail_id):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

