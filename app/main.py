from fastapi import FastAPI

from app.api.v1.user import router as user


app = FastAPI(
    title='CollabHubBR - GitHub Integration',
    summary='API de integração, meio-de-campo entre o CollabHubBR e o GitHub.',
    description='Esta API possibilita a integração com o GitHub de forma controlada'
    'e personalizada, enquanto retorna apenas os dados necessários para o '
    'funcionamento da plataforma.',
)


@app.get('/')
def root() -> dict[str, list[dict[str, str]]]:
    endpoint_list: list[tuple[str, str]] = [
        ('/', 'List possible endpoints'),
        ('/docs', 'Swagger-based documentation'),
        ('/api/v1', 'API version 1'),
    ]

    return {
        'endpoints': [
            {'endpoint': data[0], 'description': data[1]} for data in endpoint_list
        ]
    }


app.include_router(user)
