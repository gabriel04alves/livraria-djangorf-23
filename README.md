# Livraria API - Django Rest Framework

Este projeto foi desenvolvido como parte do tutorial do professor Marco André Mendes, seguindo a branch de 2023. Seu objetivo é fornecer uma API para gerenciamento de uma livraria, utilizando Django Rest Framework (DRF).

> **Atenção:** Este projeto foi criado para fins de estudo. Por isso, o código contém diversos comentários e anotações ao longo do desenvolvimento.

## Repositório

- Repositório original do tutorial: [django-drf-tutorial](https://github.com/marrcandre/django-drf-tutorial)

## Tecnologias Utilizadas

- Python
- Django
- Django Rest Framework (DRF)
- SQLite
- PDM 

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gabriel04alves/livraria-djangorf-23.git
   cd livraria-djangorf-23
   ```

2. **Instale as dependências usando PDM:**
   ```bash
   pdm install
   ```

3. **Aplique as migrações:**
   ```bash
   pdm run python manage.py migrate
   ```

4. **Crie um superusuário (opcional, para acessar o admin):**
   ```bash
   pdm run python manage.py createsuperuser
   ```

5. **Execute o servidor de desenvolvimento:**
   ```bash
   pdm run python manage.py runserver
   ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Considerações Finais

Este projeto serviu como um aprendizado sobre Django Rest Framework e desenvolvimento de APIs. 
