# Importa funções principais do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configurações de conexão com o banco de dados
SERVER = "localhost"                                # Nome do servidor (aqui, máquina local)
DATABASE = "trooperAPI_db"                          # Nome do banco de dados
DRIVER = "ODBC+Driver+17+for+SQL+Server"            # Driver ODBC usado para conectar ao SQL Server

# Monta a string de conexão no formato que o SQLAlchemy entende
# O prefixo "mssql+pyodbc" indica que será usado SQL Server via pyodbc
# trusted_connection=yes → autenticação integrada do Windows (sem usuário/senha explícitos)
SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
)

# Cria o objeto Engine, responsável por gerenciar a comunicação com o banco
# Ele sabe como abrir conexões quando necessário                                       | A variável Engine assume um papel semelhante ao conn
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma fábrica de sessões (SessionLocal) para interagir com o banco
# autocommit=False → exige commit manual para salvar alterações
# autoflush=False → evita envio automático de alterações antes de consultas
# bind=engine → vincula a sessão ao engine criado acima
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a classe base para os modelos (tabelas)
# Todas as classes que representam tabelas devem herdar de Base
Base = declarative_base()

# Adicione isso ao final do database.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
