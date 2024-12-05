from src.routers import router as product_router
from fastapi import FastAPI

app = FastAPI()


api_version_prefix = "/api/v1"

app.include_router(product_router, prefix=f"{api_version_prefix}")
