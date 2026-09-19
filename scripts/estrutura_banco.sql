USE MASTER

CREATE DATABASE trooperAPI_db

USE trooperAPI_db

-- 1. TABELA DE PATENTES
CREATE TABLE patentes_tb (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(30) NOT NULL UNIQUE,
    hierarquia_nivel INT NOT NULL -- Ex: 1 para Trooper, 2 para Corporal, 3 para Sergeant...
);

-- 2. Tabela de Esquadrões
CREATE TABLE esquadroes_tb (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    especialidade VARCHAR(50) NOT NULL -- Ex: 'Assalto', 'Reconhecimento', 'Operações Especiais'
);

-- 3. Tabela Principal de Stormtroopers (Relacionada)
CREATE TABLE stormtroopers_tb (
    id INT IDENTITY(1,1) PRIMARY KEY,
    identificacao VARCHAR(20) NOT NULL UNIQUE, -- Ex: 'TK-421'
    patente_id INT NOT NULL,
    esquadrao_id INT NOT NULL,
    precisao_tiro_pct FLOAT NOT NULL,
    batimento_cardiaco_bpm INT NOT NULL,
    status_servico VARCHAR(20) DEFAULT 'Ativo',
    
    -- Definição das Chaves Estrangeiras (Foreign Keys)
    CONSTRAINT FK_Stormtroopers_Patentes FOREIGN KEY (patente_id) REFERENCES patentes_tb(id),
    CONSTRAINT FK_Stormtroopers_Esquadroes FOREIGN KEY (esquadrao_id) REFERENCES esquadroes_tb(id)
);
GO

-- ============================================================================
-- REFERÊNCIA DE DADOS ESPERADOS PARA POPULAR O BANCO DE DADOS
-- ============================================================================

-- Esquadrões Esperados:
-- 1. 501st Legion (Especialidade: Linha de Frente / Operações Especiais)
-- 2. 212th Attack Battalion (Especialidade: Assalto Frontal)
-- 3. Inferno Squad (Especialidade: Operações Clandestinas de Elite)
-- 4. Coruscant Guard (Especialidade: Segurança Imperial e Patrulha)
-- 5. Skystrike Academy (Especialidade: Suporte Aéreo e Tático)

-- Patentes Existentes:
-- 1. Trooper (Nível Hierárquico: 1)
-- 2. Corporal (Nível Hierárquico: 2)
-- 3. Sergeant (Nível Hierárquico: 3)
-- 4. Lieutenant (Nível Hierárquico: 4)
-- 5. Commander (Nível Hierárquico: 5)



INSERT INTO esquadroes_tb (nome, especialidade)
VALUES 
('501st Legion', 'Linha de Frente / Operações Especiais'),
('212th Attack Battalion', 'Assalto Frontal'),
('Inferno Squad', 'Operações Clandestinas de Elite'),
('Coruscant Guard', 'Segurança Imperial e Patrulha'),
('Skystrike Academy', 'Suporte Aéreo e Tático')

SELECT * FROM esquadroes_tb


INSERT INTO patentes_tb (nome, hierarquia_nivel)
VALUES 
('Trooper','1'),
('Corporal','2'),
('Sergeant','3'),
('Lieutenant','4'),
('Commander','5')

GO 

SELECT * FROM patentes_tb

-- Proporções Operacionais e Hierárquicas

-- 1. Distribuição por Esquadrão (% da Força Total)

-- Coruscant Guard (40%): Guarnição massiva da capital e segurança interna.

-- 212th Attack Battalion (30%): Batalhão de infantaria pesada de linha de frente.

-- 501st Legion (18%): Legião de elite de resposta rápida.

-- Skystrike Academy (8%): Pilotos e especialistas de suporte tático.

-- Inferno Squad (2%): Unidade ultra-restrita de operações clandestinas.


-- 2. Distribuição por Patente (% do Esquadrão)

-- Trooper (65%): Base da pirâmide (1 a cada 1,5 soldados).

-- Corporal (20%): Cabos e líderes de esquadra (1 a cada 5 soldados).

-- Sergeant (10%): Sargentos de grupamento (1 a cada 10 soldados).

-- Lieutenant (4.5%): Oficiais de campo (1 a cada 22 soldados).

-- Commander (0.5%): Comandantes de unidade (1 a cada 200 soldados).

-----------------------------------------------------------------------------------------


