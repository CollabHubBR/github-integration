from typing import Final

from pydantic import BaseModel

from app.schemas.error import ErrorPayload
from app.schemas.project import ProjectPayload
from app.schemas.user import GithubUserData, GithubUserRepos


class DefaultPayload(BaseModel):
    error: bool
    data: (
        ErrorPayload
        | ProjectPayload
        | GithubUserData
        | list[GithubUserRepos]
        | dict[str, list[dict[str, str]]]
    )


__all__: Final[list[str]] = [
    'DefaultPayload',
    'ProjectPayload',
    'GithubUserData',
    'GithubUserRepos',
    'ErrorPayload',
]
