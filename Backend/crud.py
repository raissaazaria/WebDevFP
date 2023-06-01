from sqlalchemy.orm import Session
from pydantic import EmailStr, BaseModel
import models

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: EmailStr, password = str):
    db_user = models.User(email=user, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.get(models.User, user_id)
    db.delete(db_user)
    db.commit()
    return db_user

class PurchaseCreate(BaseModel):
    user_id: int
    purchase_id: int
    Name: str
    Quantity: int
    Status: str
    
class sellerCreate(BaseModel):
    user_id: int
    product_id: int
    Name: str
    Quantity: int
    Status: str

#adding item for purchasing
def add_Purchase(db: Session, product: PurchaseCreate):
    db_purchase = models.Product(Name=product.name, Quantity=product.Quantity, Status = product.Status, user_id = product.user_id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

#adding item for selling
def add_Purchase(db: Session, product: PurchaseCreate):
    db_purchase = models.Product(Name=product.name, Quantity=product.Quantity, Status = product.Status, user_id = product.user_id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

#getimage using id
def get_product_seller(db: Session, product_id: int):
    return db.query(models.seller).filter(models.seller.product_id == product_id).first()

def get_product_purchase(db: Session, purchase_id: int):
    return db.query(models.Purchase).filter(models.Purchase.purchase_id == purchase_id).first()

#productidnya & purchaseid blum di set,
#masih bingung command buat foreign key, primary key hubunginnya