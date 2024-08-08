
# Flix API

## Descrição

Flix API é uma aplicação backend desenvolvida em Python utilizando o framework Django, destinada ao gerenciamento de informações sobre filmes, atores, gêneros e reviews.

## Funcionalidades

- **Gerenciamento de Filmes**: CRUD para filmes, incluindo detalhes como título, diretor, data de lançamento, etc.
- **Gerenciamento de Atores**: CRUD para atores com informações biográficas.
- **Gerenciamento de Gêneros**: CRUD para diferentes gêneros de filmes.
- **Sistema de Reviews**: CRUD para avaliações de filmes pelos usuários.

## Requisitos

- Python 3.8+
- Django 3.2+
- PostgreSQL (ou outro banco de dados suportado)

## Instalação

1. Clone o repositório:
```
bash
git clone https://github.com/pasklan/flix-api.git
cd flix-api
```

2. Crie e ative um ambiente virtual:
  ```bash
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  ```

3. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

4. Execute as migrações do banco de dados:
  ```bash
  python manage.py migrate
  ```

5. Inicie o servidor de desenvolvimento:
  ```bash
  python manage.py runserver
  ```

## Uso

Após iniciar o servidor, a API estará disponível em `http://127.0.0.1:8000/`. Utilize ferramentas como Postman ou cURL para interagir com os endpoints.

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Todas as contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


Este arquivo fornece uma visão geral do projeto, orientações para instalação e uso, além de informações sobre como contribuir. Se precisar de ajustes ou quiser adicionar mais detalhes, é só avisar!