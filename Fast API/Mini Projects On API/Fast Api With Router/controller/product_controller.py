from fastapi import APIRouter
from service import product_service

router = APIRouter(prefix="/products")

@router.get("/{item}")
def get_item(item:str):
    pro = product_service.get_product(item)
    print(f"pro ===> {pro}")
    return pro