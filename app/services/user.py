from typing import cast

import requests as req

from app.schemas.user import GithubUserData, GithubUserRepos


def get_github_user_data_view(username: str) -> GithubUserData:
    return cast(
        GithubUserData, req.get(f'https://api.github.com/users/{username}').json()
    )


def get_github_user_repos_view(username: str) -> list[GithubUserRepos]:
    return cast(
        list[GithubUserRepos],
        req.get(f'https://api.github.com/users/{username}/repos').json(),
    )
