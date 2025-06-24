# File: `user.py`

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

### `#!py import get_github_user_data_controller`

Path: `#!py app.services.user`

Category: Local

??? example "SNIPPET"

    ```py
    from app.services.user import get_github_user_data_controller
    ```

### `#!py import get_github_user_repos_controller`

Path: `#!py app.services.user`

Category: Local

??? example "SNIPPET"

    ```py
    from app.services.user import get_github_user_repos_controller
    ```



---

## Consts

### `#!py PREFIX`

Type: `#!py Final[str]`

Value: `#!py '/api/v1/user'`

??? example "SNIPPET"

    ```py
    PREFIX: Final[str] = '/api/v1/user'
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
        endpoint_list: list[tuple[str, str]] = [('/', 'List possible endpoints'), ('/{username}', "Returns GitHub's user data"), ('/{username}/repos', 'Returns user repos')]
        return DefaultPayload(error=False, data={'endpoints': [{'endpoint': f'{PREFIX}{data[0]}', 'description': data[1]} for data in endpoint_list]})
    ```

### `#!py def get_github_user_data_view`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py router.get('/{username}')`

Args: `#!py username: str, _response: FastAPIResponse`

Kwargs: `#!py None`

The "View" of a MVC arch for this endpoint.

By receiving the username, this coroutine calls it's "Controller" equivalent
for data processing; just a way to handle internal structure.


:param username: Owner of the repository.

:type username: str

:param _response: Internal var for handling status code.

:type _response: fastapi.Response

:returns: DefaultPayload with the user data.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    @router.get('/{username}')
    async def get_github_user_data_view(username: str, _response: FastAPIResponse) -> DefaultPayload:
        """
        The "View" of a MVC arch for this endpoint.

        By receiving the username, this coroutine calls it's "Controller" equivalent
        for data processing; just a way to handle internal structure.

        :param username: Owner of the repository.
        :type username: str
        :param _response: Internal var for handling status code.
        :type _response: fastapi.Response
        :returns: DefaultPayload with the user data.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        return await get_github_user_data_controller(username, _response)
    ```

### `#!py def get_github_user_repos_view`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py router.get('/{username}/repos')`

Args: `#!py username: str, _response: FastAPIResponse`

Kwargs: `#!py None`

The "View" of a MVC arch for this endpoint.

By receiving the username, this coroutine calls it's "Controller" equivalent
for data processing; just a way to handle internal structure.


:param username: Owner of the repository.

:type username: str

:param _response: Internal var for handling status code.

:type _response: fastapi.Response

:returns: DefaultPayload with the user's repos.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    @router.get('/{username}/repos')
    async def get_github_user_repos_view(username: str, _response: FastAPIResponse) -> DefaultPayload:
        """
        The "View" of a MVC arch for this endpoint.

        By receiving the username, this coroutine calls it's "Controller" equivalent
        for data processing; just a way to handle internal structure.

        :param username: Owner of the repository.
        :type username: str
        :param _response: Internal var for handling status code.
        :type _response: fastapi.Response
        :returns: DefaultPayload with the user's repos.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        return await get_github_user_repos_controller(username, _response)
    ```



---

## Assertions

!!! info "NO ASSERT DEFINED HERE"
