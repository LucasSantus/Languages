
-- Dropando o database "convidados", caso existir
DROP DATABASE IF EXISTS convidados;

-- Criando database "convidados", caso não existir
CREATE DATABASE IF NOT EXISTS convidados;

-- Utilizando banco de dados "convidados"
use convidados;

-- Criando tabela "pessoas", caso não existir
CREATE TABLE IF NOT EXISTS `pessoas`(
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL COMMENT 'email não é obrigatório',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com o nome das pessoas convidadas';

-- Criando tabela "presentes", caso não existir
CREATE TABLE IF NOT EXISTS `presentes` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `descricao` varchar(100) NOT NULL,
  `valor` double unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


 -- Visualizar o script, como foi criado a tabela
/*
	SHOW CREATE TABLE nome_tabela; 
*/

-- Selecionar tabela
/*
	SELECT * FROM nome_banco-de-dados.nome_tabela;
*/

-- Inserindo na tabela
/*
	SELECT * FROM nome_banco-de-dados.nome_tabela;
*/



-- insert into pessoas(nome,email) values('Thiago','tiago.@at.com.br'); -- insere uma linha de dados

-- insert into pessoas(nome,email) values -- insert de uma conjunto de dados (vários)
-- ('maria','maria@gmail.com'),
-- ('joao','joao@gmail.com');

-- select em desenvolvimento
-- select de todos atributos.
-- select * from pessoas;

-- select ideal para produção.
-- select de determinados atributos e não todos.
-- select id, nome, email from pessoas; 


-- select email from pessoas; --  selecionando somente o atributo email da tabela pessoas.

-- select nome as nome_completo, email as contato, id as codigo_pessoa from pessoas; -- Select usando apelidos nos atributos.

-- select nome as `Nome Completo`, email as `Contato`, id as `Chave Primária` from pessoas; -- Select usando apelidos nos atributos.

-- select id, nome, email from pessoas where id = 1; -- select com filtos.

-- select id, nome, email from pessoas where id <> 1; -- select com filtro de diferente 

-- select id, nome, email from pessoas where id >2 ; -- select com filtro de maior

-- usando filtos para registro 

-- select id, nome, email from pessoas where id = 1; igual a 1

-- select id, nome, email from pessoas where id <> 2; diferente que 2

-- select id, nome, email from pessoas where id > 2; maior que 2

-- select id, nome, email from pessoas where id = 2 or id = 4; retorna o registro 2 e 4

-- select id, nome, email from pessoas where id in(2,1,4,5,6,8,7); -- select de varios valores  (especificos) 

-- select id, nome, email from pessoas where nome = 'Thiago'; -- select por nome (String)

-- select id, nome, email from pessoas where nome like 'Thiago'; -- filtrando por nomes parecidos (like).

-- % no inicio significa "que termine com" 
-- select id, nome, email from pessoas where nome like '%Thiago'; -- filtando com %

-- % no final significa "que inicie com"
-- select id, nome, email from pessoas where nome like 'Thiago%'; -- filtando com %


-- %% no inicio e no final significa "que contenha em algum lugar"

-- select id, nome, email from pessoas where email like '%.com%';

-- select * from pessoas;


