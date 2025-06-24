from typing import Any

from fastapi import Response as FastAPIResponse
from fastapi import status
from httpx import AsyncClient

from app.schemas.error import ErrorType
from app.schemas.payload import DefaultPayload, ErrorPayload, GithubUserData
from app.utils import GITHUB_API_URL


async def get_github_user_data_controller(
    username: str, _response: FastAPIResponse
) -> DefaultPayload:
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
        return DefaultPayload(
            error=True,
            data=ErrorPayload(
                error_type=ErrorType.GitHubFetchError,
                error=f'No GitHub account found for {username = }',
            ),
        )
    except KeyError:
        return DefaultPayload(
            error=False,
            data=GithubUserData(**data),
        )


async def get_github_user_repos_controller(
    username: str, _response: FastAPIResponse
) -> DefaultPayload:
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
        return DefaultPayload(
            error=True,
            data=ErrorPayload(
                error_type=ErrorType.GitHubFetchError,
                error=f'No GitHub account found for {username = }',
            ),
        )
    except TypeError:
        return DefaultPayload(
            error=False,
            data=data,
        )
