select * from pessoas;

-- realizando um delete
delete from pessoas where id = 10; -- modo seguro
delete from pessoas where nome = "Maria"; -- modo sem segurança

-- update
update pessoas set nome = "Thiago Giovanella" where id = 1;
update pessoas set nome = 'José da Silva', email = 'jose@hotmail.com'
where id = 3;