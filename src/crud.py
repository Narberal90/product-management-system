from sqlalchemy import select
from src.models import Product, Category
from src.schemas import ProductCreate, ProductUpdate, CategoryCreate

from sqlalchemy.ext.asyncio import AsyncSession


async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
        category_id=product.category_id,
    )
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def get_product(db: AsyncSession, product_id: int):
    query = select(Product).filter(Product.id == product_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def update_product(
        db: AsyncSession,
        product_id: int,
        product: ProductUpdate
):
    db_product = await get_product(db, product_id)
    if db_product:
        if product.name:
            db_product.name = product.name
        if product.description:
            db_product.description = product.description
        if product.price:
            db_product.price = product.price
        if product.quantity is not None:
            db_product.quantity = product.quantity
        if product.category_id:
            db_product.category_id = product.category_id
        await db.commit()
        await db.refresh(db_product)
    return db_product


async def delete_product(db: AsyncSession, product_id: int):
    db_product = await get_product(db, product_id)
    if db_product:
        await db.delete(db_product)
        await db.commit()
    return db_product


async def create_category(db: AsyncSession, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


async def get_category(db: AsyncSession, category_id: int):
    result = await db.execute(
        select(Category)
        .filter(Category.id == category_id)
    )
    return result.scalar_one_or_none()


async def delete_category(db: AsyncSession, category_id: int):
    db_category = await get_category(db, category_id)
    if db_category:
        await db.delete(db_category)
        await db.commit()
    return db_category
