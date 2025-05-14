BANCO DE DADOS


-- Tabela de Pacientes
CREATE TABLE Paciente (
    id_paciente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo CHAR(1),
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco TEXT
);

-- Tabela de Profissionais de Saúde
CREATE TABLE Profissional (
    id_profissional SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    registro_profissional INT, 
    especialidade VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela de Agendamentos de Consulta
CREATE TABLE AgendamentoConsulta (
    id_agendamento SERIAL PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_profissional INT NOT NULL,
    data_hora TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'Agendada',
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_profissional) REFERENCES ProfissionalSaude(id_profissional)
);

-- Tabela de Prontuários Médicos
CREATE TABLE Prontuario (
    id_prontuario SERIAL PRIMARY KEY,
    id_paciente INT NOT NULL,
    data_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT,
    diagnostico TEXT,
    prescricao TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);

insert into Paciente(nome,cpf,data_nascimento,sexo,telefone,email) 
values("João da Silva","125.654.897-54","1985-12-25","M","51998658799","joaodasilva@gmail.com");

insert into Paciente(nome,cpf,data_nascimento,sexo,telefone,email) 
values("Maria Pereira","525.584.874-11","1991-05-18","F","51985476215","mariapereira@gmail.com");

insert into Paciente(nome,cpf,data_nascimento,sexo,telefone,email) 
values("Geovana Ribeiro","254.325.125-87","1997-02-27","F","51965478521","geovanaribeiro@gmail.com");

insert into Profissional(nome,cpf,registro_profissional,especialidade,telefone,email) values("Felipe Faguntes","124.121.452-25","458787","Neurologista","51998547865","felipefagundes@gmail.com")