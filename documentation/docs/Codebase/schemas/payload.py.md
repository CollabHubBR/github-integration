# File: `payload.py`

Role: Python Source Code

Path: `..app.schemas`

No file docstring provided.

---

## Imports

### `#!py import Final`

Path: `#!py typing`

Category: Native

??? example "SNIPPET"

    ```py
    from typing import Final
    ```

### `#!py import BaseModel`

Path: `#!py pydantic`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from pydantic import BaseModel
    ```

### `#!py import ErrorPayload`

Path: `#!py app.schemas.error`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.error import ErrorPayload
    ```

### `#!py import ProjectPayload`

Path: `#!py app.schemas.project`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.project import ProjectPayload
    ```

### `#!py import GithubUserData`

Path: `#!py app.schemas.user`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.user import GithubUserData
    ```

### `#!py import GithubUserRepos`

Path: `#!py app.schemas.user`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.user import GithubUserRepos
    ```



---

## Consts

!!! info "NO CONSTANT DEFINED HERE"

---

## Classes

### `#!py class DefaultPayload`

Parents: `BaseModel`

Decorators: `#!py None`

Kwargs: `#!py None`

No `docstring` provided.

??? example "SNIPPET"

    ```py
    class DefaultPayload(BaseModel):
        error: bool
        data: ErrorPayload | ProjectPayload | GithubUserData | list[GithubUserRepos] | dict[str, list[dict[str, str]]]
    ```



---

## Functions

!!! info "NO FUNCTION DEFINED HERE"

---

## Assertions

!!! info "NO ASSERT DEFINED HERE"
