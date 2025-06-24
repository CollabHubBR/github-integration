from typing import Final

from fastapi import APIRouter
from fastapi import Response as FastAPIResponse

from app.schemas.payload import DefaultPayload
from app.services.user import (
    get_github_user_data_controller,
    get_github_user_repos_controller,
)


PREFIX: Final[str] = '/api/v1/user'


router = APIRouter(prefix=PREFIX, tags=['user'])


@router.get('/')
async def endpoints() -> DefaultPayload:
    """
    The hub of this endpoint family.

    Just gets nothing and return all the endpoints of this sub-path.

    :returns: DefaultPayload with the existing endpoints.
    :rtype: app.schemas.payload.DefaultPayload
    :raises: Nothing
    """

    endpoint_list: list[tuple[str, str]] = [
        ('/', 'List possible endpoints'),
        ('/{username}', "Returns GitHub's user data"),
        ('/{username}/repos', 'Returns user repos'),
    ]

    return DefaultPayload(
        error=False,
        data={
            'endpoints': [
                {'endpoint': f'{PREFIX}{data[0]}', 'description': data[1]}
                for data in endpoint_list
            ]
        },
    )


@router.get('/{username}')
async def get_github_user_data_view(
    username: str, _response: FastAPIResponse
) -> DefaultPayload:
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


@router.get('/{username}/repos')
async def get_github_user_repos_view(
    username: str, _response: FastAPIResponse
) -> DefaultPayload:
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
