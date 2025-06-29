# CollabHubBR - GitHub Integration

![GitHub License](https://img.shields.io/github/license/CollabHubBR/github-integration?labelColor=101010)

<!-- ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/CollabHubBR/github-integration/testing.yml?style=flat&labelColor=101010) -->

Este repositório contém o código-fonte do **Microsserviço de Integração GitHub API** do **CollabHubBR**, a plataforma brasileira de coordenação e organização de projetos de código-aberto. Desenvolvido em **Python** com o framework **FastAPI**, este serviço é crucial para enriquecer a experiência do usuário, buscando e processando dados diretamente do GitHub.

A principal responsabilidade deste microsserviço é **buscar dados de repositórios** do GitHub para serem apresentados na página do projeto no CollabHubBR. Isso inclui tanto informações gerais do repositório (estrelas, forks, descrição, linguagens, etc.) quanto dados para compor os dashboards de métricas (commits, issues, pull requests, contribuidores). Para garantir acesso seguro e abrangente, o serviço utiliza a **GitHub API**, com suporte para autenticação via **Chave Privada** (GitHub Apps) quando necessário, permitindo a recuperação de informações mais detalhadas e ações específicas. Os dados são processados e, quando aplicável, persistidos no **PostgreSQL** para otimização e histórico.

## Stack

![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD43B)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

![pytest](https://img.shields.io/badge/pytest-0094e7.svg?style=for-the-badge&logo=pytest&logoColor=ffffff)

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=000&color=fff)

![uv](https://img.shields.io/badge/uv-2b0231?style=for-the-badge&logo=uv)
![Ruff](https://img.shields.io/badge/Ruff-2b0231?style=for-the-badge&logo=ruff)
![Swagger](https://img.shields.io/badge/Swagger-004400?style=for-the-badge&logo=swagger&logoColor=00ff00)
![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-fff?style=for-the-badge&logo=material-for-mkdocs&logoColor=526cfe)

![GitHub](https://img.shields.io/badge/GitHub-fff?style=for-the-badge&logo=github&logoColor=181717)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-fff?style=for-the-badge&logo=github-pages&logoColor=222222)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088ff?style=for-the-badge&logo=github-actions&logoColor=fff)

## Arquitetura

A arquitetura do Microsserviço de Integração GitHub API do CollabHubBR segue os princípios de microsserviços, com foco em **processamento eficiente de dados externos** e **integração segura**. Adotamos uma estrutura modular para organizar nossos modelos, rotas, serviços, repositórios e configurações, visando a clareza e a facilidade de manutenção.

```mermaid
flowchart TD

    A[Outros Microsserviços] --> B{API Gateway}
    B --> C[Microsserviço de Integração GitHub API]
    C --> D(Controller/Router)
    D --> E(Services)
```

Para todos os efeitos, a API considera o retorno através da estrutura abaixo, padronizando a interpretação de quando um retorno ocorrer da forma esperada ou não com `app.schemas.payload.DefaultPayload`:

```py
{
  "error": bool,
  "data": {...}
}
```

Onde `"error"` indica simplesmente se o retorno foi um sucesso ou não, enquanto `"data"` indica o corpo da resposta, tanto em caso de sucesso, variando conforme endpoint, ou em caso de erro, seguindo a estrutura a seguir:

```json
{
  "error": true,
  "data": {
    "error_type": "GitHubFetchError",
    "error": "No result found for username = 'username' and repo = 'repo"
  }
}
```

Os tipos de erros catalogados podem ser encontrados em `app.schemas.payload.ErrorType`, um `enum.Enum` nativo do Python.

### Estrutura de Pastas

Abaixo, descrevemos a organização principal das pastas do projeto:

- `app/`: Contém todo o código-fonte da aplicação.
  - `api/`: Definição das rotas e endpoints da API (FastAPI `APIRouter`).
    - `v1/`: Versões da API.
      - `{filename}.py`: Arquivos para cada grupo de endpoints (ex: `user.py`).
  - `schemas/`: Modelos Pydantic para validação de entrada e saída de dados.
  - `services/`: Lógica de negócio e interações com a GitHub API.
    - `{filename}.py`: Funções para interagir com a GitHub API (autenticação, requisições).
  - `utils.py`: Funções utilitárias e helpers (ex: constante da API do GitHub).
  - `main.py`: Ponto de entrada principal da aplicação FastAPI.
- `tests/`: Arquivos para testes unitários e de integração.

### Instalação de Dependências

```bash
uv sync
```

### Servidor Local

```bash
uv run task dev
```

### Servidor de Prod

```bash
uv run fastapi run
```

### Execução de Testes

```bash
uv run pytest
```

### Linter

```bash
uv run task lint
```

### Recriar Documentação

```bash
uv run task doc
```

## To-Do List

Confira a [To-Do List aqui](https://github.com/CollabHubBR/github-integration/blob/main/.github/TODO.md)

## Contrib

Antes de contribuir ativamente com o projeto é **fortemente recomendada** a leitura dos documentos abaixo:

- [Código de Conduta](https://github.com/CollabHubBR/.github/blob/main/CODE_OF_CONDUCT.md)
- [Contribuindo](https://github.com/CollabHubBR/.github/blob/main/CONTRIBUTING.md)
- [Segurança](https://github.com/CollabHubBR/.github/blob/main/SECURITY.md)
- [Suporte](https://github.com/CollabHubBR/.github/blob/main/SUPPORT.md)

## Licença

This project is under [MIT - Massachusetts Institute of Technology](https://choosealicense.com/licenses/mit/). A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
