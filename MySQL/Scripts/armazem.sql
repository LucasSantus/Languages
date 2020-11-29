drop database if exists armazem;

create database if not exists armazem;
use armazem;

-- drop table if exists produtos;
create table if not exists produtos(
id int unsigned not null primary key auto_increment,
descricao varchar(100) not null,
valor float not null,
estoque float null
);

-- drop table if exists vendas;
create table if not exists vendas(
id int unsigned not null primary key auto_increment,
idproduto int unsigned not null,
valor float not null,
qtd float not null,
constraint fk_idproduto_vendas foreign key(idproduto)
references produtos(id) on delete restrict on update cascade
);

-- drop table if exists log;
create table if not exists log(
id int unsigned not null primary key auto_increment,
datahora datetime default current_timestamp,
descricao varchar(250) not null,
idproduto int unsigned not null,
constraint fk_idproduto_log foreign key(idproduto)
references produtos(id) on delete restrict on update cascade
);


INSERT INTO armazem.produtos (descricao, valor, estoque) VALUES 
('Soja', '5', '5000'),
('Milho', '10', '1000'),
('Café', '12', '3000'),
('Feijão', '7', '200');

select * from produtos;

drop trigger if exists trg_baixa_estoque;

delimiter $$

create trigger trg_baixa_estoque after insert 
on vendas 
for each row
begin

update produtos set estoque = (estoque - NEW.qtd) where id = NEW.idproduto;

end $$

delimiter ;

insert into vendas(idproduto, valor, qtd) values(2, 10, 50);

select * from produtos;
