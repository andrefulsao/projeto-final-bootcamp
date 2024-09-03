from sqlalchemy import Session
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
    #transformar minha view para ORM
    db_product = ProductModel(**product.model_dump())
    #adicionar na tabela
    db.add(db_product)
    #commitar na minha tabela
    db.commit()
    #fazer o refresh do banco de dados
    db.refresh()
    #retornar para o usuario o item criado
    return db_product