# File: `project.py`

Role: Python Source Code

Path: `..app.api.v1`

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

### `#!py import APIRouter`

Path: `#!py fastapi`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from fastapi import APIRouter
    ```

### `#!py import Response`

Path: `#!py fastapi`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from fastapi import Response
    ```

### `#!py import DefaultPayload`

Path: `#!py app.schemas.payload`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.payload import DefaultPayload
    ```

### `#!py import get_global_repo_data_controller`

Path: `#!py app.services.project`

Category: Local

??? example "SNIPPET"

    ```py
    from app.services.project import get_global_repo_data_controller
    ```



---

## Consts

### `#!py PREFIX`

Type: `#!py Final[str]`

Value: `#!py '/api/v1/project'`

??? example "SNIPPET"

    ```py
    PREFIX: Final[str] = '/api/v1/project'
    ```



---

## Classes

!!! info "NO CLASS DEFINED HERE"

---

## Functions

### `#!py def endpoints`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py router.get('/')`

Args: `#!py None`

Kwargs: `#!py None`

The hub of this endpoint family.

Just gets nothing and return all the endpoints of this sub-path.


:returns: DefaultPayload with the existing endpoints.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    @router.get('/')
    async def endpoints() -> DefaultPayload:
        """
        The hub of this endpoint family.

        Just gets nothing and return all the endpoints of this sub-path.

        :returns: DefaultPayload with the existing endpoints.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        endpoint_list: list[tuple[str, str]] = [('/', 'List possible endpoints'), ('/{username}/{repo}', 'Returns repo general content')]
        return DefaultPayload(error=False, data={'endpoints': [{'endpoint': f'{PREFIX}{data[0]}', 'description': data[1]} for data in endpoint_list]})
    ```

### `#!py def get_global_repo_data_view`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py router.get('/{username}/{repo}')`

Args: `#!py username: str, repo: str, _response: FastAPIResponse`

Kwargs: `#!py None`

The "View" of a MVC arch for this endpoint.

By receiving the username and a repository, this coroutine calls it's "Controller"
equivalent for data processing; just a way to handle internal structure.


:param username: Owner of the repository.

:type username: str

:param repo: Repository's name itself.

:type repo: str

:param _response: Internal var for handling status code.

:type _response: fastapi.Response

:returns: DefaultPayload with the repo data.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    @router.get('/{username}/{repo}')
    async def get_global_repo_data_view(username: str, repo: str, _response: FastAPIResponse) -> DefaultPayload:
        """
        The "View" of a MVC arch for this endpoint.

        By receiving the username and a repository, this coroutine calls it's "Controller"
        equivalent for data processing; just a way to handle internal structure.

        :param username: Owner of the repository.
        :type username: str
        :param repo: Repository's name itself.
        :type repo: str
        :param _response: Internal var for handling status code.
        :type _response: fastapi.Response
        :returns: DefaultPayload with the repo data.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        return await get_global_repo_data_controller(username, repo, _response)
    ```



---

## Assertions

!!! info "NO ASSERT DEFINED HERE"
