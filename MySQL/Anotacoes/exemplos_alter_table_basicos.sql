create table edicoes(
	id int not null primary key auto_increment,
    descricao varchar(100) not null,
    valor float not null comment "valor do ingresso desta edição",
    data_inicial datetime not null,
    data_final datetime not null,
    lotacao int null default 200
);

-- alterando atributo de entidade
alter table edicoes 
change descricao titulo varchar(100) not null;

alter table edicoes 
add column descricao text null;

alter table edicoes
change column lotacao vagas int null default 200,
add column local varchar(200) not null
after titulo;

/*
Adicionar:
atributo: inicio_vendas, não nulo
atributo: maximo_desconto (percentual) não nulo após o valor
atributo: ativo (S/N) default 'S' no final
*/

alter table edicoes 
add column inicio_vendas datetime null default current_timestamp after valor,
add column maximo_desconto float not null after valor,
-- add column ativo char null default 'S'
-- add column ativo boolean null default 1
-- add column ativo enum('S','N') null default 'S'
add column ativo bit null default 1;

alter table edicoes change column inicio_vendas inicio_vendas datetime not null;
alter table edicoes drop column maximo_desconto;






