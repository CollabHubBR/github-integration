# File: `user.py`

Role: Python Source Code

Path: `..app.services`

No file docstring provided.

---

## Imports

### `#!py import Any`

Path: `#!py typing`

Category: Native

??? example "SNIPPET"

    ```py
    from typing import Any
    ```

### `#!py import Response`

Path: `#!py fastapi`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from fastapi import Response
    ```

### `#!py import status`

Path: `#!py fastapi`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from fastapi import status
    ```

### `#!py import AsyncClient`

Path: `#!py httpx`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from httpx import AsyncClient
    ```

### `#!py import ErrorType`

Path: `#!py app.schemas.error`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.error import ErrorType
    ```

### `#!py import DefaultPayload`

Path: `#!py app.schemas.payload`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.payload import DefaultPayload
    ```

### `#!py import ErrorPayload`

Path: `#!py app.schemas.payload`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.payload import ErrorPayload
    ```

### `#!py import GithubUserData`

Path: `#!py app.schemas.payload`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.payload import GithubUserData
    ```

### `#!py import GITHUB_API_URL`

Path: `#!py app.utils`

Category: Local

??? example "SNIPPET"

    ```py
    from app.utils import GITHUB_API_URL
    ```



---

## Consts

!!! info "NO CONSTANT DEFINED HERE"

---

## Classes

!!! info "NO CLASS DEFINED HERE"

---

## Functions

### `#!py def get_github_user_data_controller`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py None`

Args: `#!py username: str, _response: FastAPIResponse`

Kwargs: `#!py None`

Gets and returns every user's data.

By receiving the username, this coroutine fetches the GitHub API for the data
about that user


:param username: Owner of the repository.

:type username: str

:param _response: Internal var for handling status code.

:type _response: fastapi.Response

:returns: DefaultPayload with the data mentioned above.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    async def get_github_user_data_controller(username: str, _response: FastAPIResponse) -> DefaultPayload:
        """
        Gets and returns every user's data.

        By receiving the username, this coroutine fetches the GitHub API for the data
        about that user

        :param username: Owner of the repository.
        :type username: str
        :param _response: Internal var for handling status code.
        :type _response: fastapi.Response
        :returns: DefaultPayload with the data mentioned above.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        async with AsyncClient() as client:
            data: Any = await client.get(f'{GITHUB_API_URL}/users/{username}')
            data = data.json()
        try:
            assert data['status'] == '404'
            _response.status_code = status.HTTP_404_NOT_FOUND
            return DefaultPayload(error=True, data=ErrorPayload(error_type=ErrorType.GitHubFetchError, error=f'No GitHub account found for username = {username!r}'))
        except KeyError:
            return DefaultPayload(error=False, data=GithubUserData(**data))
    ```

### `#!py def get_github_user_repos_controller`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py None`

Args: `#!py username: str, _response: FastAPIResponse`

Kwargs: `#!py None`

Gets and returns every user's repos.

By receiving the username, this coroutine fetches the GitHub API for
every repository from that username.


:param username: Owner of the repository.

:type username: str

:param _response: Internal var for handling status code.

:type _response: fastapi.Response

:returns: DefaultPayload with the data mentioned above.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    async def get_github_user_repos_controller(username: str, _response: FastAPIResponse) -> DefaultPayload:
        """
        Gets and returns every user's repos.

        By receiving the username, this coroutine fetches the GitHub API for
        every repository from that username.

        :param username: Owner of the repository.
        :type username: str
        :param _response: Internal var for handling status code.
        :type _response: fastapi.Response
        :returns: DefaultPayload with the data mentioned above.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        async with AsyncClient() as client:
            data: Any = await client.get(f'{GITHUB_API_URL}/users/{username}/repos')
            data = data.json()
            print(data)
        try:
            assert data['status'] == '404'
            _response.status_code = status.HTTP_404_NOT_FOUND
            return DefaultPayload(error=True, data=ErrorPayload(error_type=ErrorType.GitHubFetchError, error=f'No GitHub account found for username = {username!r}'))
        except TypeError:
            return DefaultPayload(error=False, data=data)
    ```



---

## Assertions

### `#!py assert data['status'] == '404'`

Message: `#!py None`

??? example "SNIPPET"

    ```py
    assert data['status'] == '404'
    ```

### `#!py assert data['status'] == '404'`

Message: `#!py None`

??? example "SNIPPET"

    ```py
    assert data['status'] == '404'
    ```


