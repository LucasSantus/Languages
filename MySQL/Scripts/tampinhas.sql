create schema colecaotampinhas;
use colecaotampinhas;

create table fabricantes(
id int not null primary key auto_increment,
descricao varchar(100) not null,
ativo tinyint null default 1
);

create table produtos(
id int not null primary key auto_increment,
idfabricante int not null,
descricao varchar(100) not null,
anofabricacao YEAR not null,
modelo varchar(100) not null,
edicao varchar(100) not null,
constraint fk_prod_fabricante foreign key(idfabricante)
references fabricantes(id) on delete restrict on update cascade
);

create table tampinhas(
id int not null primary key auto_increment,
idproduto int not null,
descricao varchar(200) not null,
anolancamento YEAR not null,
foto blob null,
constraint fk_tampinha_produto foreign key(idproduto)
references produtos(id) on delete restrict on update cascade
);







