from pydantic import BaseModel


class ProjectPayload(BaseModel):
    full_name: str
    language: str
    description: str
    homepage: str
    readme: str
    open_issues_count: int
    forks_count: int
