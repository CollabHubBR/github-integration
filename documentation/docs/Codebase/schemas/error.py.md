# File: `error.py`

Role: Python Source Code

Path: `..app.schemas`

No file docstring provided.

---

## Imports

### `#!py import Enum`

Path: `#!py enum`

Category: Native

??? example "SNIPPET"

    ```py
    from enum import Enum
    ```

### `#!py import BaseModel`

Path: `#!py pydantic`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from pydantic import BaseModel
    ```



---

## Consts

!!! info "NO CONSTANT DEFINED HERE"

---

## Classes

### `#!py class ErrorType`

Parents: `Enum`

Decorators: `#!py None`

Kwargs: `#!py None`

No `docstring` provided.

??? example "SNIPPET"

    ```py
    class ErrorType(Enum):
        APIError = 'APIInternalError'
        GitHubFetchError = 'GitHubFetchError'
    ```

### `#!py class ErrorPayload`

Parents: `BaseModel`

Decorators: `#!py None`

Kwargs: `#!py None`

No `docstring` provided.

??? example "SNIPPET"

    ```py
    class ErrorPayload(BaseModel):
        error_type: ErrorType
        error: str
    ```



---

## Functions

!!! info "NO FUNCTION DEFINED HERE"

---

## Assertions

!!! info "NO ASSERT DEFINED HERE"
