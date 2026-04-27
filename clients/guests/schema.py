"""Pydantic-схемы для API гостей."""
import random

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Any
from faker import Faker

fake = Faker('ru_RU')


class GuestsData(BaseModel):
    id: int
    hotel_id: int
    first_name: str | int
    middle_name: str | int | None
    last_name: str | int
    email: str | None
    phone: str | int | None
    type: int | None
    gender: int | None
    birthdate: datetime | None
    birth_country_id: int | None
    citizenship_country_id: int | None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None


class GuestData(GuestsData):
    levelBenefit: Dict[str, Any] | None
    isEnabledLevelAdd: bool
    level: Dict[str, Any] | None
    extra: Dict[str, Any] | None
    tags: List | None


class PaginationMeta(BaseModel):
    current_page: int
    total: int
    last_page: int


class GetGuestsResponseSchema(BaseModel):
    data: List[GuestsData]
    meta: PaginationMeta


class GetGuestResponseSchema(BaseModel):
    data: GuestData


class CreateGuestRequestSchema(BaseModel):
    firstName: str = Field(default_factory=fake.first_name)
    middleName: str | None = Field(default_factory=fake.middle_name)
    lastName: str = Field(default_factory=fake.last_name)
    email: str = Field(default_factory=fake.email)
    phone: str = Field(default_factory=fake.phone_number)
    type: int = Field(default_factory=lambda: random.randint(1, 2))
    gender: int = Field(default_factory=lambda: random.randint(1, 2))
    birthdate: str = Field(default_factory=lambda: str(fake.date_of_birth()))
    birthCountryId: int = Field(default_factory=lambda: fake.random_int(min=1, max=250))
    citizenshipCountryId: int = Field(default_factory=lambda: fake.random_int(min=1, max=250))
    extra: Any | None = None
    addresses: Any | None = None
    docs: Any | None = None
    tags: Any | None = None


class CreateGuestResponseSchema(BaseModel):
    data: int
