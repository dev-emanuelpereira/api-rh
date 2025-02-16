# API RH

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## Introdução

API responsável para cadastrar usuários, vagas de emprego e curriculos. É possível também candidatar usuários e currículos nas vagas criadas. 
## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Exemplos](#exemplos)

## Instalação

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
- [Python](https://nodejs.org/) v3.12 ou superior

### Passos para Instalação

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
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

### Requisições

Para as requisições HTTP utilize as seguintes variáveis:

```plaintext
PORT=5000
BASEURL=http://127.0.0.1
```
## Uso
Para iniciar o servidor de desenvolvimento, execute na raiz do projeto:

```bash
python app.py
```
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
