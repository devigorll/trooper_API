# Trooper API

API REST desenvolvida em **Python com FastAPI** para gerenciamento de Stormtroopers, patentes e esquadrões do Império Galáctico.

O projeto foi desenvolvido com foco em praticar a criação de APIs, integração com banco de dados, organização de código e arquitetura em camadas.

## Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* SQL Server
* PyODBC
* Uvicorn
* Pandas
* NumPy

## Funcionalidades

A API permite realizar operações de:

* Cadastro, consulta, atualização e exclusão de Stormtroopers
* Cadastro, consulta, atualização e exclusão de Patentes
* Cadastro, consulta, atualização e exclusão de Esquadrões
* Relacionamento entre Stormtroopers, Patentes e Esquadrões
* Validação de dados através do Pydantic
* Integração com SQL Server através do SQLAlchemy
* Documentação automática através do Swagger

## Estrutura do projeto

```text
trooper_API/
│
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   │
│   ├── routers/
│   │   ├── esquadrao_router.py
│   │   ├── patente_router.py
│   │   └── stormtrooper_router.py
│   │
│   ├── schemas/
│   │   ├── esquadrao_schema.py
│   │   ├── patente_schema.py
│   │   └── stormtrooper_schema.py
│   │
│   └── services/
│       ├── esquadrao_service.py
│       ├── patente_service.py
│       └── stormtrooper_service.py
│
├── scripts/
│   ├── estrutura_banco.sql
│   └── inserir_dados.ipynb
│
├── requirements.txt
└── README.md
```

## Banco de dados

O projeto utiliza **SQL Server** e possui três tabelas principais:

### Patentes

Armazena as patentes dos Stormtroopers e seus respectivos níveis hierárquicos.

Exemplos:

* Trooper
* Corporal
* Sergeant
* Lieutenant
* Commander

### Esquadrões

Armazena os esquadrões e suas especialidades.

Exemplos:

* 501st Legion
* 212th Attack Battalion
* Inferno Squad
* Coruscant Guard
* Skystrike Academy

### Stormtroopers

Tabela principal da aplicação.

Cada Stormtrooper possui:

* Identificação
* Patente
* Esquadrão
* Precisão de tiro
* Batimento cardíaco
* Status de serviço

As tabelas são relacionadas através de **chaves estrangeiras**.

## Arquitetura

O projeto foi organizado separando as principais responsabilidades da aplicação:

**Routers**

Responsáveis pelas rotas e requisições HTTP.

**Schemas**

Responsáveis pela validação e estrutura dos dados utilizando Pydantic.

**Services**

Responsáveis pelas operações de negócio e comunicação com o banco de dados.

**Models**

Representam as tabelas do banco utilizando SQLAlchemy.

**Database**

Responsável pela configuração da conexão com o SQL Server e gerenciamento das sessões.

Essa separação facilita a organização e manutenção do código.

## Endpoints

### Stormtroopers

```text
GET     /stormtroopers/
GET     /stormtroopers/{id}
POST    /stormtroopers/
PUT     /stormtroopers/{id}
DELETE  /stormtroopers/{id}
```

### Patentes

```text
GET     /patentes/
GET     /patentes/{id}
POST    /patentes/
PUT     /patentes/{id}
DELETE  /patentes/{id}
```

### Esquadrões

```text
GET     /esquadroes/
GET     /esquadroes/{id}
POST    /esquadroes/
PUT     /esquadroes/{id}
DELETE  /esquadroes/{id}
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/devigorll/trooper_API.git
```

Entre na pasta:

```bash
cd trooper_API
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Execute o script:

```text
scripts/estrutura_banco.sql
```

Ele cria o banco `trooperAPI_db` e suas respectivas tabelas.

O projeto está configurado inicialmente para utilizar:

```text
Servidor: localhost
Banco: trooperAPI_db
Driver: ODBC Driver 17 for SQL Server
Autenticação: Windows
```

Caso sua configuração do SQL Se
