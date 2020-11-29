

-- insert into pessoas(nome,email) values('Thiago','tiago.@at.com.br'); -- insere uma linha de dados

-- insert into pessoas(nome,email) values -- insert de uma conjunto de dados (vários)
-- ('maria','maria@gmail.com'),
-- ('joao','joao@gmail.com');

-- select * from pessoas;

-- select id, nome, email from pessoas; -- select de determinados atributos e não todos.

-- select email from pessoas; --  selecionando somente o atributo email da tabela pessoas.

-- select nome as nome_completo, email as contato, id as codigo_pessoa from pessoas; -- Select usando apelidos nos atributos.

-- select id, nome, email from pessoas where id = 1; -- select com filtos.

-- select id, nome, email from pessoas where id <> 1; -- select com filtro de diferente 

-- select id, nome, email from pessoas where id >2 ; -- select com filtro de maior

-- usando filtos para mais de um registro 
-- select id, nome, email from pessoas where id = 2 or id = 4;

-- select id, nome, email from pessoas where id in(2,1,4,5,6,8,7); -- select de varios valores  (especificos) 

-- select id, nome, email from pessoas where nome = 'Thiago'; -- select por nome (String)

-- select id, nome, email from pessoas where nome like 'Thiago'; -- filtrando por nomes parecidos (like).

-- select id, nome, email from pessoas where nome like '%Thiago'; -- filtando com %

-- % no inicio significa "que termine com"  -- % no final significa "que inicie com"

-- %% no inicio e no final significa "que contenha"

-- select id, nome, email from pessoas where email like '%.com%';

-- select * from pessoas;





-- delete

-- delete from pessoas where id = 1; -- Deletando pelo id (chave primaria) MODO SEGURO


-- delete from pessoas where nome='joao'; -- NÃO DÁ CERTO... TEM QUE SER PELA CHAVE PRIMARIA

-- insert into pessoas (nome,email) values ("abner", "abner.luiz@tjmg.jus.br");

-- UPDATE 

	-- update pessoas set nome = "thiago giovanela" where id = 2; -- ATUALIZAR DADO NA TABELA (UNICO VALOR)
    
    -- update pessoas set nome = "jose da silva", email = "jose@hotmail.com" where id = 4; -- ATUALIZANDO VARIOS VALORES NA TABELA


-- delete from tabela ...; -- deletar a tupla (dados)





-- drop -- para deletar a entidade


-- Eliminar entidades
-- drop table presentes; 

-- Elinar toda a base de dados
-- drop database convidados;
-- drop schema convidados;


-- delete from tabela ...; -- deletar a tupla (dados)

-- drop -- para deletar a entidade


-- Eliminar entidades
-- drop table presentes; 

-- Elinar toda a base de dados
-- drop database convidados;
-- drop schema convidados;

-- create schema festas;

-- use festas;


/* -- CRIANÇÃO DA TABELA EDIÇÕES
create table if not exists edicoes(
	id int not null primary key auto_increment,
    descricao varchar(100) not null,
    valor float  not null comment "Valor do ingresso desta edição",
    data_inicial datetime not null,
    data_final datetime not null,
    lotacao int null default 200
);
*/


-- ALTERAÇÃO DE ATRIBUTOS NA ENTIDADE
-- alter table edicoes
-- change descricao titulo varchar(100) not null;

-- ADD O ATRIBUTOS NA TABELA (ULTIMA POSICAO)
-- alter table edicoes
-- add column descricao text null 

/*
-- ALTERAÇÃO E ADD DE ATRIBUTOS NA TABELA 
alter table edicoes
change column lotacao vagas int null default 200,
add column local varchar(200) not null
after titulo;
*/

/*
-- ADICIONANDO VALORES NA TABELA
alter table edicoes
add column inicio_vendas datetime not null,
add column maximo_desconto int not null comment "percentual"
after valor,
add column ativo bool default 1;
*



TAMPINHAS 

create database tampinhas;
use tampinhas;

create table if not exists fabricante(
	id int not null primary key auto_increment,
    nome varchar(100) not null,
    localidade varchar (200) not null,
    telefone varchar (20) not null,
    email varchar(100) null
);

create table if not exists tampinha(
	id int not null primary key auto_increment,
    nome varchar(100) not null,
    ano_lancamento int not null,
    idproduto int not null,
    constraint fk_tampinha_produto foreign key(idproduto)
    references produto(id) on delete restrict on update cascade
    
);

create table if not exists produto(
	id int not null primary key auto_increment,
    nome varchar(100) not null,
    modelo varchar(100) not null,
    edicao  varchar(100) not null,
    idfabricante int not null,
    constraint fk_produto_fabricante foreign key(idfabricante)
    references fabricante(id) on delete restrict on update cascade
    
);