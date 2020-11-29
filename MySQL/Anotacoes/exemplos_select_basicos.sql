-- em desenvolvimento, retorna todos os atributos
select * from pessoas;

-- ideal
select id, nome, email from pessoas;
select email from pessoas;
select email, nome, id from pessoas;

-- dando apelidos para os atributos
-- com caracteres especiais
select nome as `Nome Completo`, email as `E-mail`, 
id as `Identificação` from pessoas;

-- usando filtros
select id, nome, email from pessoas where id = 1;
select id, nome, email from pessoas where id <> 1;
select id, nome, email from pessoas where id > 2;
select id, nome, email from pessoas where id >= 2;

-- usando filtros para mais de um registro
select id, nome, email from pessoas where id = 2 or id = 4;
select id, nome, email from pessoas 
where id in(2,4,5,6,7,10,14,19,20,33);

-- filtrando por texto 
select id, nome, email from pessoas where nome = 'Thiago';
select id, nome, email from pessoas where nome like 'Thiago';
-- % no final significa "que comece com"
select id, nome, email from pessoas where email like 'j%';
-- % no início significa "que termine com"
select id, nome, email from pessoas where nome like '%o';
-- %% no início e no final significa "que contenha"
select id, nome, email from pessoas where email like '%.com%';


/*
= igual
> maior
< menor
<> diferente
and e
or ou
*/

