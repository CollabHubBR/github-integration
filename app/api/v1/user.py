from typing import Final

from fastapi import APIRouter

from app.schemas.user import GithubUserData, GithubUserRepos
from app.services.user import get_github_user_data_view, get_github_user_repos_view


PREFIX: Final[str] = '/api/v1/user'


router = APIRouter(prefix=PREFIX, tags=['user'])


@router.get('/')
def endpoints() -> dict[str, list[dict[str, str]]]:
    endpoint_list: list[tuple[str, str]] = [
        ('/', 'List possible endpoints'),
        ('/{username}', "Returns GitHub's user data"),
        ('/{username}/repos', 'Returns user repos'),
    ]

    return {
        'endpoints': [
            {'endpoint': f'{PREFIX}{data[0]}', 'description': data[1]}
            for data in endpoint_list
        ]
    }


@router.get('/{username}')
def get_github_user_data(username: str) -> GithubUserData:
    return get_github_user_data_view(username)


@router.get('/{username}/repos')
def get_github_user_repos(username: str) -> list[GithubUserRepos]:
    return get_github_user_repos_view(username)
