from fastapi import FastAPI

from app.api.v1.project import router as project
from app.api.v1.user import router as user
from app.schemas.payload import DefaultPayload


app = FastAPI(
    title='CollabHubBR - GitHub Integration',
    summary='API de integração, meio-de-campo entre o CollabHubBR e o GitHub.',
    description='Esta API possibilita a integração com o GitHub de forma controlada '
    'e personalizada, enquanto retorna apenas os dados necessários para o '
    'funcionamento da plataforma.',
    version='1.0.0',
)


@app.get('/')
async def root() -> DefaultPayload:
    """
    The hub of the main endpoint family.

    Just gets nothing and return all the endpoints of this master path.

    :returns: DefaultPayload with the existing endpoints.
    :rtype: app.schemas.payload.DefaultPayload
    :raises: Nothing
    """

    endpoint_list: list[tuple[str, str]] = [
        ('/', 'List possible endpoints'),
        ('/docs', 'Swagger-based documentation'),
        ('/api/v1', 'API version 1'),
    ]

    return DefaultPayload(
        error=False,
        data={
            'endpoints': [
                {'endpoint': data[0], 'description': data[1]} for data in endpoint_list
            ]
        },
    )


app.include_router(user)
app.include_router(project)
