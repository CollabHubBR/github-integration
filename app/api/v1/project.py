from typing import Final

from fastapi import APIRouter
from fastapi import Response as FastAPIResponse

from app.schemas.payload import DefaultPayload
from app.services.project import get_global_repo_data_controller


PREFIX: Final[str] = '/api/v1/project'


router = APIRouter(prefix=PREFIX, tags=['project'])


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
        ('/{username}/{repo}', 'Returns repo general content'),
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


@router.get('/{username}/{repo}')
async def get_global_repo_data_view(
    username: str, repo: str, _response: FastAPIResponse
) -> DefaultPayload:
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
