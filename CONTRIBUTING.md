# Contribuindo

## Setup

```bash
git clone https://github.com/joaopalmeidao/chromedriver_manager.git
cd chromedriver-version-manager

pip install uv
uv sync
```

## Estrutura do projeto

```
chromedriver_manager/
├── __init__.py
└── module/
    ├── manager.py          # classe principal ChromeDriverManager
    ├── config/
    │   ├── logger.py       # configuração de logging
    │   └── settings.py     # constantes e diretórios
    └── core/
        └── utils.py        # funções auxiliares (API, download, extração)
```

## Publicando no PyPI

1. Atualize a versão em `pyproject.toml`
2. Faça o build e o upload:

```bash
uv build
twine upload dist/*
```
