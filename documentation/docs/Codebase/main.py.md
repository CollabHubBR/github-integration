# File: `main.py`

Role: Python Source Code

Path: `..app`

No file docstring provided.

---

## Imports

### `#!py import FastAPI`

Path: `#!py fastapi`

Category: 3rd Party

??? example "SNIPPET"

    ```py
    from fastapi import FastAPI
    ```

### `#!py import router`

Path: `#!py app.api.v1.project`

Category: Local

??? example "SNIPPET"

    ```py
    from app.api.v1.project import router
    ```

### `#!py import router`

Path: `#!py app.api.v1.user`

Category: Local

??? example "SNIPPET"

    ```py
    from app.api.v1.user import router
    ```

### `#!py import DefaultPayload`

Path: `#!py app.schemas.payload`

Category: Local

??? example "SNIPPET"

    ```py
    from app.schemas.payload import DefaultPayload
    ```



---

## Consts

### `#!py app`

Type: `#!py Unknown`

Value: `#!py FastAPI(title='CollabHubBR - GitHub Integration', summary='API de integração, meio-de-campo entre o CollabHubBR e o GitHub.', description='Esta API possibilita a integração com o GitHub de forma controlada e personalizada, enquanto retorna apenas os dados necessários para o funcionamento da plataforma.', version='1.0.0')`

??? example "SNIPPET"

    ```py
    app = FastAPI(title='CollabHubBR - GitHub Integration', summary='API de integração, meio-de-campo entre o CollabHubBR e o GitHub.', description='Esta API possibilita a integração com o GitHub de forma controlada e personalizada, enquanto retorna apenas os dados necessários para o funcionamento da plataforma.', version='1.0.0')
    ```



---

## Classes

!!! info "NO CLASS DEFINED HERE"

---

## Functions

### `#!py def root`

Type: `#!py Coroutine`

Return Type: `#!py DefaultPayload`

Decorators: `#!py app.get('/')`

Args: `#!py None`

Kwargs: `#!py None`

The hub of the main endpoint family.

Just gets nothing and return all the endpoints of this master path.


:returns: DefaultPayload with the existing endpoints.

:rtype: app.schemas.payload.DefaultPayload
:raises: Nothing

??? example "SNIPPET"

    ```py
    @app.get('/')
    async def root() -> DefaultPayload:
        """
        The hub of the main endpoint family.

        Just gets nothing and return all the endpoints of this master path.

        :returns: DefaultPayload with the existing endpoints.
        :rtype: app.schemas.payload.DefaultPayload
        :raises: Nothing
        """
        endpoint_list: list[tuple[str, str]] = [('/', 'List possible endpoints'), ('/docs', 'Swagger-based documentation'), ('/api/v1', 'API version 1')]
        return DefaultPayload(error=False, data={'endpoints': [{'endpoint': data[0], 'description': data[1]} for data in endpoint_list]})
    ```



---

## Assertions

!!! info "NO ASSERT DEFINED HERE"
