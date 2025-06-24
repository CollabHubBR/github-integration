from enum import Enum

from pydantic import BaseModel


class ErrorType(Enum):
    APIError = 'APIInternalError'
    GitHubFetchError = 'GitHubFetchError'


class ErrorPayload(BaseModel):
    error_type: ErrorType
    error: str
