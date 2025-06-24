# File: `project.py`

Role: Python Source Code

Path: `..app.schemas`

No file docstring provided.

---

## Imports

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

### `#!py class ProjectPayload`

Parents: `BaseModel`

Decorators: `#!py None`

Kwargs: `#!py None`

No `docstring` provided.

??? example "SNIPPET"

    ```py
    class ProjectPayload(BaseModel):
        full_name: str
        language: str
        description: str
        homepage: str
        readme: str
        open_issues_count: int
        forks_count: int
    ```



---

## Functions

!!! info "NO FUNCTION DEFINED HERE"

---

## Assertions

!!! info "NO ASSERT DEFINED HERE"
