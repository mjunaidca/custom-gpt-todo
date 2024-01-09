from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Union

class TODOBase(BaseModel):
    """
    Represents a TODO in the database.
    """
    title: str
    description: Union[str, None] = None
    completed: bool = False

class TODOCreate(TODOBase):
    """
    Represents a TODO item to be created.
    """
    id: UUID

class TODOResponse(TODOBase):
    """
    Represents a TODO item to be returned.
    """
    id: UUID
    created_at: datetime
    updated_at: datetime