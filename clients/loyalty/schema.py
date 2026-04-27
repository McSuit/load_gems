"""Pydantic-схемы для API настроек лояльности."""
from pydantic import BaseModel
from typing import List, Dict, Any


class LoyaltyLevels(BaseModel):
    loyaltySetting: Dict[str, Any] | None
    levels: List[Dict[str, Any] | None]


class GetLoyaltySettingsResponseSchema(BaseModel):
    data: LoyaltyLevels