# Encurtador de URL - Flask API

Este projeto é uma API de encurtador de URL desenvolvida em Python com Flask, seguindo princípios SOLID e KISS. Utiliza SQLite como banco de dados e oferece operações CRUD, redirecionamento automático, validação de URL, documentação Swagger e testes automatizados.

## Funcionalidades
- Criar URLs encurtadas
- Listar todas as URLs
- Buscar, atualizar e remover URLs pelo short_url
- Redirecionamento automático ao acessar /<short_url>
- Validação de formato de URL
- Documentação interativa em Swagger (OpenAPI)
- Testes automatizados com unittest

## Instalação
1. Clone o repositório:
   ```bash
   git clone <repo_url>
   cd estudos
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como rodar
1. Crie o banco de dados (opcional, pois será criado automaticamente ao rodar a API):
   ```bash
   python main.py
   ```
2. Acesse a API em: http://127.0.0.1:5000/
3. Documentação Swagger: http://127.0.0.1:5000/docs

## Exemplos de uso
### Criar uma URL encurtada
```http
POST /urls
Content-Type: application/json
{
  "original_url": "https://www.google.com"
}
```

### Redirecionar
Acesse: `http://127.0.0.1:5000/<short_url>`

### Listar URLs
```http
GET /urls
```

## Testes
Execute todos os testes automatizados:
```bash
python -m unittest test_url_shortener.py
```

## Estrutura
- `main.py`: Código principal da API
- `test_url_shortener.py`: Testes automatizados
- `requirements.txt`: Dependências
- `static/swagger.json`: Especificação OpenAPI
- `.gitignore`: Arquivos ignorados pelo git

## Licença
MIT

