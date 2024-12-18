# pydantic-sqlalchemy-type-decorator
Seamlessly use Pydantic 2 models in a Postgres SQLAlchemy model

## Installation

The package is available on [pypi](https://pypi.org/p/pydantic_sqlalchemy_deco).

You can install this package using pip:

```bash
pip install pydantic_sqlalchemy_deco
```

### Requirements

This library requires:
- Pydantic 2+
- SQLAlchemy (2.0+?)
- Postgres with JSONB support

Other versions may be supported as well, but please open an [issue](https://github.com/kevinhikaruevans/pydantic-sqlalchemy-type-decorator/issues) if you run into any problems.

## Usage

Given some Pydantic model called `MyCustomModel`, you can specify your columns like:

```python
from pydantic_sqlalchemy_deco.decorator import PydanticJSON

...

# Define Pydantic model somewhere:
class MyCustomModel(BaseModel):
    custom_id: int = 0


# Define your SQLAlchemy model:
class MyEntry(Base):

    custom_data: Mapped[MyCustomModel] = mapped_column(PydanticJSON(MyCustomModel))
```

Then, you can use the `custom_data` column as you'd expect:

```python
entry = MyEntry(
    custom_data=MyCustomModel(custom_id=1234)
)

...

print(entry.custom_data.custom_id)

```


# BaseModel changes

If your `BaseModel` has custom serializers, you can specify this using the `T` parameter:

```python
    custom_data: Mapped[MyCustomModel] = mapped_column(PydanticJSON[CoolerBaseModel](MyCustomModel))
```
