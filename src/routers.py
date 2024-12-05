from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src import crud, schemas
from src.database.session import get_db

router = APIRouter()


@router.post("/products/", response_model=schemas.Product)
async def create_product(
        product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_product(db=db, product=product)


@router.get("/products/{product_id}", response_model=schemas.Product)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await crud.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=schemas.Product)
async def update_product(
        product_id: int,
        product: schemas.ProductCreate,
        db: AsyncSession = Depends(get_db)
):
    db_product = await crud.update_product(
        db=db, product_id=product_id, product=product
    )
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


@router.post("/categories/", response_model=schemas.Category)
async def create_category(
        category: schemas.CategoryCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_category(db=db, category=category)


@router.get("/categories/{category_id}", response_model=schemas.Category)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    db_category = await crud.get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.delete("/categories/{category_id}")
async def delete_category(
        category_id: int,
        db: AsyncSession = Depends(get_db)
):
    db_category = await crud.delete_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
