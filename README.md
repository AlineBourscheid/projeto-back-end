
# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Este projeto tem como objetivo o desenvolvimento de uma API RESTful para o gerenciamento de pacientes, profissionais, agendamentos e prontuários em uma instituição de saúde, utilizando Django, Django REST Framework e autenticação OAuth2.

## Tecnologias Utilizadas

- Python 3.8
- Django 4.1.13
- Django REST Framework 3.14.0
- Django OAuth Toolkit 2.3.0
- MariaDB (Banco de Dados)

## Funcionalidades

- Cadastro e gerenciamento de pacientes, profissionais, agendamentos e prontuários
- API RESTful com endpoints para operações CRUD (GET, POST, PUT, PATCH, DELETE)
- Autenticação segura com OAuth2
- Proteção de rotas com autenticação obrigatória
- Criação de usuários e autenticação via formulário personalizado

##  Instalação

1. Clone o repositório:
```bash
git clone https://github.com/alinebourscheid/projeto-back-end.git
cd sghss_api
```

2. Crie um ambiente virtual e ative:
```bash
python3.8 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python3.8 manage.py migrate
```

5. Crie um superusuário:
```bash
python3.8 manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python3.8 manage.py runserver
```

## Autenticação OAuth2

Para obter um token de autenticação, utilize:

```bash
curl -X POST -d "grant_type=password&username=aline&password=aline" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
```

E para acessar endpoints protegidos:

```bash
curl -H "Authorization: Bearer <seu_token>" http://localhost:8000/paciente/
```

## Estrutura Básica

- `models.py` - Contém os modelos: `Paciente`, `Profissional`, `CadastroAgendamento`, `Prontuario`
- `serializers.py` - Serialização dos dados para a API
- `views.py` - Views baseadas em classes genéricas
- `urls.py` - Rotas da aplicação, incluindo OAuth2
- `settings.py` - Configurações da aplicação, autenticação e permissões

## Exemplo de Endpoint

Listar e criar pacientes:
```http
GET /paciente/
POST /paciente/
```

Atualizar, deletar ou visualizar um paciente específico:
```http
GET /paciente/<id>/
PUT /paciente/<id>/
PATCH /paciente/<id>/
DELETE /paciente/<id>/
```

## Cadastro via formulário (Signup)

```bash
curl http://127.0.0.1:8000/signup/ -X POST -d "username=aline2&password1=aline%40teste1&password2=aline%40teste1"
```

---


