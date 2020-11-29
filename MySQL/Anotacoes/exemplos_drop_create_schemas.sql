-- eliminando uma entidade
-- drop table presentes;

-- eliminando toda a base de dados
-- drop database convidados;
-- drop schema convidados;

create schema festas;
use festas;

create table edicoes(
	id int not null primary key auto_increment,
    descricao varchar(100) not null,
    valor float not null comment "valor do ingresso desta edição",
    data_inicial datetime not null,
    data_final datetime not null,
    lotacao int null default 200
);






