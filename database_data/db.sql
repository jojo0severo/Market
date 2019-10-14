CREATE TABLE Ano (
  nome_ano INTEGER(4) PRIMARY KEY
);

CREATE TABLE Mes (
  nome_mes NUMBER(2) NOT NULL,
  nome_ano NUMBER(4) NOT NULL,
  PRIMARY KEY (nome_mes, nome_ano),
  CONSTRAINT fk_mes_ano FOREIGN KEY (nome_ano) REFERENCES Ano (nome_ano)
    ON DELETE CASCADE
);

CREATE TABLE Venda (
  valor    NUMBER    PRIMARY KEY,
  nome_mes NUMBER(2) NOT NULL,
  nome_ano NUMBER(4) NOT NULL,
  CONSTRAINT fk_compra_mes FOREIGN KEY (nome_mes, nome_ano) REFERENCES Mes (nome_mes, nome_ano)
    ON DELETE CASCADE
);

CREATE TABLE Compra (
  valor    NUMBER    PRIMARY KEY,
  nome_mes NUMBER(2) NOT NULL,
  nome_ano NUMBER(4) NOT NULL,
  CONSTRAINT fk_compra_mes FOREIGN KEY (nome_mes, nome_ano) REFERENCES Mes (nome_mes, nome_ano)
    ON DELETE CASCADE
);