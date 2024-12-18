import sys
from typing import Any, Type, Optional, TypeVar
from pydantic import BaseModel
from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects.postgresql import JSONB

if sys.version_info >= (3, 13):
    T = TypeVar('T', bound=BaseModel, default=BaseModel)
else:
    T = TypeVar('T', bound=BaseModel)

class PydanticJSON(TypeDecorator[T]):
    impl = JSONB

    def __init__(self, pydantic_model: Type[T]) -> None:
        """
        Initializes the custom type with the Pydantic model to use for serialization/deserialization.

        :param pydantic_model: The Pydantic model class to use for JSON handling.
        """
        
        super().__init__()

        self.pydantic_model = pydantic_model

    def process_bind_param(self, value: Optional[T], dialect: Any) -> Optional[Any]:
        if value is None:
            return None
        
        if isinstance(value, self.pydantic_model):
            return value.model_dump()
        
        raise ValueError(f"Expected a {self.pydantic_model.__name__} instance or None, got {type(value)}")

    def process_result_value(self, value: Optional[Any], dialect: Any) -> Optional[T]:
        if value is None:
            return None
        
        return self.pydantic_model.model_validate(value)  # Parse JSON string into Pydantic model
