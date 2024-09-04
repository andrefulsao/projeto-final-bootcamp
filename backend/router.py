from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()

@router.get("/products/", response_model=List[ProductResponse])
def route_read_all_products(db: Session = Depends(get_db)):
    """Read all products"""
    products = get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def route_read_one_product(product_id:int, db: Session = Depends(get_db)):
    """Read one product"""
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="ID do produto não existente")
    
    return db_product

@router.post("/products/", response_model=ProductResponse)
def route_create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Create one product"""
    return create_product(product=product, db=db)

@router.delete("/products/{product_id}", response_model=ProductResponse)
def route_delete_product(product_id:int, db: Session = Depends(get_db)):
    """Delete one product"""
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="ID do produto não existente")        
    return product_db


@router.put("/products/{product_id}", response_model=ProductResponse)
def route_update_product(product_id:int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Não foi possível realizar a alteração.")
    return product_db