# API RH – Sistema de Recrutamento e Seleção
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

API REST desenvolvida em **Python** com o objetivo de simular um **sistema de RH**, permitindo o gerenciamento de usuários, vagas de emprego, currículos e candidaturas.  
O projeto foi criado com foco em **boas práticas de APIs REST**, **organização de código** e **regras de negócio**.

---

## Visão Geral

A API possibilita o cadastro de usuários, criação de vagas de emprego, registro de currículos e candidatura de usuários às vagas disponíveis.

O projeto tem caráter **educacional** e foi desenvolvido para consolidar conhecimentos em desenvolvimento backend, modelagem de dados e comunicação via HTTP.

---

## Tecnologias Utilizadas

- **Python 3.12**
- **Flask**
- **API REST**
- **Virtual Environment (venv)**
- **JSON para troca de dados**

---

## Funcionalidades

- Cadastro e gerenciamento de usuários
- Criação e gerenciamento de vagas de emprego
- Cadastro e atualização de currículos
- Candidatura de usuários a vagas
- Consulta de permissões (roles)
- Validação básica de dados

---

## Instalação e Execução

### Pré-requisitos

- [Python](https://www.python.org/) 3.12 ou superior
- pip

### Passo a passo

1. Clone o repositório:
    ```bash
    git clone https://github.com/dev-emanuelpereira/api-rh.git
    cd api-rh
    ```

2. Inicie o ambiente virtual:
    ```bash
    cd ambvir
    Scripts\activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor:
```bash
python app.py
```

A aplicação estará disponível em:
```bash
http://127.0.0.1:5000
```

## Configuração

Para as requisições HTTP utilize as seguintes variáveis:

```plaintext
PORT=5000
BASEURL=http://127.0.0.1
```
---

## Endpoints

### Visão Geral

### Roles
| Método | Endpoint          | Descrição                          |
|--------|--------------------|------------------------------------|
| **GET**    | /roles   | Retorna todas as permissões          |

#### Usuarios
| Método | Endpoint          | Descrição                          |
|--------|--------------------|------------------------------------|
| **GET**    | /usuario?usuario_id=:id   | Retorna o usuario com seu curriculo e sua permissão          |
| **POST**   | /usuario   | Cria um novo usuario              |
| **PUT**    | /usuario?usuario_id=:id  | Atualiza o usuario       |
| **DELETE** | /usuario?usuario_id=1 | Exclui o usuario existente        |

#### Vagas
| Método | Endpoint          | Descrição                          |
|--------|--------------------|------------------------------------|
| **GET**    | /vagas   | Retorna todas as vagas |
| **GET**    | /vaga?usuario_id=:id   | Retorna a vaga criada pelo usuario id          |
| **POST**   | /vaga?usuario_id=:id   | Cria uma vaga atrelada a um usuario id              |
| **PUT**    | /vaga?usuario_id=:id  | Atualiza a vaga por usuario       |
| **DELETE** | /vaga?usuario_id=:id | Exclui a vaga por usuario        |

#### Curriculo
| Método | Endpoint          | Descrição                          |
|--------|--------------------|------------------------------------|
| **GET**    | /curriculo/:id   | Retorna a curriculo criado por id          |
| **POST**   | /curriculo?usuario_id=:id   | Cria um curriculo por usuario              |
| **PUT**    | /curriculo?curriculo_id=:id  | Atualiza o curriculo por usuario       |
| **DELETE** | /curriculo?curriculo_id=:id | Exclui o curriculo por usuario        |

#### Candidatura
| Método | Endpoint          | Descrição                          |
|--------|--------------------|------------------------------------|
| **GET**    | /candidato?usuario_id=:id&vaga_id=:id   | Procurar por candidatura          |
| **POST**   | /candidato   | Cria candidatura              |
| **PUT**    | /candidato  | Atualiza candidatura       |
| **DELETE** | /candidato | Exclui a candidatura por vaga e usuario        |

## Exemplo de requisições

### Usuario
#### POST /usuario

Body
```json
{
    "nome" : "nome",
    "email" : "teste@gmail.com",
    "cpf" : "cpf valido",
    "senha" : "teste",
    "confirmar_senha" : "teste",
    "aluno" : true ou false
}
```

#### PUT /usuario?usuario_id=:id

Body
```json
{
    "nome" : "nome",
    "email" : "teste@gmail.com",
    "cpf" : "cpf valido",
    "senha" : "teste",
    "aluno" : true ou false
}
```
---
### Vagas

#### POST /vaga?usuario_id=:id 

Body
```json
{
    "nome_vaga" : "nome_vaga",
    "descricao" : "descricao",
    "requisito_formacao" : "requisito_formacao",
    "salario" : salario
}
```

#### PUT /vaga?usuario_id=:id 

Body
```json
{
    "nome_vaga" : "nome_vaga",
    "descricao" : "descricao",
    "requisito_formacao" : "requisito_formacao",
    "salario" : salario
}
```
---
### Curriculo

#### POST /curriculo?usuario_id=:id
```json
{
    "nome" : "nome",
    "formacao" : "Formacao",
    "area_atuacao" : "Area de Atuacao"
}
```

#### PUT /curriculo?usuario_id=:id
```json
{
    "nome" : "nome",
    "formacao" : "Formacao",
    "area_atuacao" : "Area de Atuacao"
}
```
---
### Candidatura

#### POST /candidato
```json
{
    "usuario_id" : usuario_id,
    "vaga_id" : vaga_id,
    "inscrever" : true or false
}
```

#### PUT /candidato
```json
{
    "usuario_id" : usuario_id,
    "vaga_id" : vaga_id,
    "inscrever" : true or false
}
```

#### DELETE /candidato
```json
{
    "usuario_id" : usuario_id,
    "vaga_id" : vaga_id,
}
```
---
## Autor
### Emanuel Pereira
- *GitHub:* https://github.com/dev-emanuelpereira
