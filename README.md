# pydantic-sqlalchemy-type-decorator
Seamlessly use Pydantic 2 models in a Postgres SQLAlchemy model

# Usage

Given some Pydantic model called `MyCustomModel`, you can specify your columns like:

```python
from pydantic_sqlalchemy_deco.decorator import PydanticJSON

...

class MyTable(Base):

    response: Mapped[MyCustomModel] = mapped_column(PydanticJSON(MyCustomModel))
```



# BaseModel changes

If your `BaseModel` has custom serializers, you can specify this using the `T` parameter:

```python
    response: Mapped[MyCustomModel] = mapped_column(PydanticJSON[CoolerBaseModel](MyCustomModel))
```