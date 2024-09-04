from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

def get_products(db: Session):
    """
        Função que retorna todos os produtos.
    """
    return db.query(ProductModel).all()

def get_product(db: Session, product_id: int):
    """
        Função que retorna as informações de um produto.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    """
        Função que recebe um product e insere no banco.
    """
    #transformar minha view para ORM
    db_product = ProductModel(**product.model_dump())
    #adicionar na tabela
    db.add(db_product)
    #commitar na minha tabela
    db.commit()
    #fazer o refresh do banco de dados
    db.refresh(db_product)
    #retornar para o usuario o item criado
    return db_product

def delete_product(db: Session, product_id: int):
    """
        Função que deleta um produto.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
        Função que atualiza um produto.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category

    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    db.refresh(db_product)
    return db_product
