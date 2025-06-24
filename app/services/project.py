from asyncio import gather
from collections.abc import Coroutine
from typing import Any

from fastapi import Response as FastAPIResponse
from fastapi import status
from httpx import AsyncClient, Response

from app.schemas.error import ErrorType
from app.schemas.payload import DefaultPayload, ErrorPayload, ProjectPayload
from app.utils import GITHUB_API_URL


async def get_global_repo_data_controller(
    username: str, repo: str, _response: FastAPIResponse
) -> DefaultPayload:
    """
    Gets the repo and it's username and returns the required data.

    By receiving the username and a repository, this coroutine fetches
    the GitHub API for the data listed below:

        - Repository's Name
        - Main Language
        - Repository's Description
        - Project's Website
        - Readme Content
        - Current Number of Issues
        - Current Number of Forks

    :param username: Owner of the repository.
    :type username: str
    :param repo: Repository's name itself.
    :type repo: str
    :param _response: Internal var for handling status code.
    :type _response: fastapi.Response
    :returns: DefaultPayload with the data mentioned above.
    :rtype: app.schemas.payload.DefaultPayload
    :raises: Nothing
    """

    urls: dict[str, str] = {
        'repo': f'/repos/{username}/{repo}',
        'readme': f'/repos/{username}/{repo}/readme',
    }

    async with AsyncClient() as client:
        tasks: dict[str, Coroutine[Any, Any, Response]] = {
            key: client.get(f'{GITHUB_API_URL}{url}') for key, url in urls.items()
        }

        responses = await gather(*tasks.values())

    result: dict[str, Any] = {
        key: response.json() for key, response in zip(tasks.keys(), responses)
    }

    try:
        return DefaultPayload(
            error=False,
            data=ProjectPayload(
                full_name=result['repo']['full_name'],
                language=result['repo']['language'],
                description=result['repo']['description'],
                homepage=result['repo']['homepage'],
                readme=result['readme']['content'],
                open_issues_count=result['repo']['open_issues_count'],
                forks_count=result['repo']['forks_count'],
            ),
        )

    except KeyError:
        _response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultPayload(
            error=True,
            data=ErrorPayload(
                error_type=ErrorType.GitHubFetchError,
                error=f'No result found for {username = } and {repo = }',
            ),
        )
