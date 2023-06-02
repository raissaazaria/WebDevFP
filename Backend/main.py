from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import EmailStr, BaseModel
import models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == user_id).first()

@app.get("/users/email/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.email == email).first()

class UserCreate(BaseModel):
    email: EmailStr
    password: str

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(models.User, user_id)
    db.delete(db_user)
    db.commit()
    return db_user

class PurchaseCreate(BaseModel):
    user_id: int
    purchase_id: int
    name: str
    quantity: int
    status: str
    
class SellerCreate(BaseModel):
    user_id: int
    product_id: int
    name: str
    quantity: int
    status: str

@app.post("/purchases")
def add_purchase(product: PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = models.Purchase(
        user_id=product.user_id,
        purchase_id=product.purchase_id,
        Name=product.name,
        Quantity=product.quantity,
        Status=product.status
    )
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

@app.post("/sellers")
def add_seller(product: SellerCreate, db: Session = Depends(get_db)):
    db_seller = models.Seller(
        user_id=product.user_id,
        product_id=product.product_id,
        Name=product.name,
        Quantity=product.quantity,
        Status=product.status
    )
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller

@app.get("/products/seller/{product_id}")
def get_product_seller(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.Seller).filter(models.Seller.product_id == product_id).first()

@app.get("/products/purchase/{purchase_id}")
def get_product_purchase(purchase_id: int, db: Session = Depends(get_db)):
    return db.query(models.Purchase).filter(models.Purchase.purchase_id == purchase_id).first()
