from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import SessionDep
from app.models import ItemCreate, ItemOut, ItemsOut, ItemUpdate, Message

router = APIRouter()


# @router.post("/", response_model=ItemsOut)
# def read_items(
#     session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
# ) -> Any:
#     """
#     Retrieve items.
#     """

