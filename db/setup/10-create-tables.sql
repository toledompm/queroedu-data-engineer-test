CREATE TABLE cities(
  city_id serial PRIMARY KEY,
  municipio INT,
  regiao INT,
  uf INT
);

CREATE TABLE contracts(
  id INT PRIMARY KEY,
  regiao INT,
  municipio INT,
  uf INT,
  cbo2002_ocupacao INT,
  subclasse INT,
  tipo_estabelecimento INT,
  tam_estab_jan INT,
  salario INT,
  horas_contratuais INT,
  tipo_empregador INT,
  ind_trab_intermitente INT,
  ind_trab_parcial INT,
  indicador_aprendiz INT,
  fonte INT,
  idade INT,
  raca_cor INT,
  sexo INT,
  tipo_de_deficiencia INT,
  grau_de_instrucao INT,
  competencia INT,
  tipo_movimentacao INT,
  saldo_movimentacao INT,
  secao CHAR,

  city_id serial,

  FOREIGN KEY (city_id)
    REFERENCES cities (city_id)
);
