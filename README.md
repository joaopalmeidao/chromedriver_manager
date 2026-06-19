# ChromeDriver Version Manager

[![PyPI version](https://img.shields.io/pypi/v/chromedriver-version-manager)](https://pypi.org/project/chromedriver-version-manager/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/chromedriver-version-manager)](https://pypi.org/project/chromedriver-version-manager/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/chromedriver-version-manager)](https://pypi.org/project/chromedriver-version-manager/)

Um gerenciador simples e eficiente para manter o **ChromeDriver** sincronizado com a versão do **Google Chrome** instalada no sistema.

Ideal para automações com Selenium que quebram frequentemente devido a atualizações automáticas do navegador.

## Funcionalidades

- **Detecção automática:** Detecta a versão exata do Chrome instalado.
- **Download inteligente:** Busca a versão compatível via API oficial do Chrome for Testing (Google Chrome Labs).
- **Cache integrado:** Evita downloads repetidos — reutiliza o driver enquanto a versão do Chrome não mudar.
- **Thread-safe:** Usa file lock para garantir segurança em ambientes com múltiplos processos simultâneos.
- **Multiplataforma:** Funciona no Windows e Linux.

## Instalação

```bash
pip install chromedriver-version-manager
```

## Uso

```python
from chromedriver_manager import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = ChromeDriverManager().get_driver_path()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
```

## Como funciona

1. Detecta a versão do Chrome instalada na máquina.
2. Consulta a [API do Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) para encontrar a versão compatível do ChromeDriver.
3. Faz o download e extrai o executável automaticamente.
4. Armazena o caminho em cache — nas próximas execuções, retorna o driver já baixado sem nova requisição.

## Pré-requisitos

- Python >= 3.9
- Google Chrome instalado
