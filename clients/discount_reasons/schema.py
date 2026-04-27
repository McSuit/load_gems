"""Pydantic-схемы для API причин скидок."""
from pydantic import BaseModel
from typing import List


class DiscountReason(BaseModel):
    id: int
    hotelId: int
    name: str
    isSystem: bool
    isDeleted: bool | None = None


class GetDiscountReasonResponse(BaseModel):
    data: DiscountReason


class GetDiscountReasonsResponse(BaseModel):
    data: List[DiscountReason]
