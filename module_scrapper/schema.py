from pydantic import BaseModel
from typing import Optional


class ValidateProduct(BaseModel):
    product_title: str
    product_price: int
    path_to_image: str


class ValidateScrapeSettings(BaseModel):
    limit_pages: Optional[int] = 1
    proxy: Optional[str] = ""


class ValidateResponseModel(BaseModel):
    status: int
    message: str
    response: dict
