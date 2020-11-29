DROP DATABASE IF EXISTS festas;

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

-- Criando tabela "pessoas", caso não existir
CREATE TABLE IF NOT EXISTS `pessoas`(
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL COMMENT 'email não é obrigatório',
  `cpf` varchar(30) NOT NULL,
  `ddd` varchar(20) NOT NULL,
  `celular` varchar(100) NULL COMMENT 'celular não é obrigatório',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com o nome das pessoas';

CREATE TABLE IF NOT EXISTS depoimentos(
    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
    `idedicao` int NOT NULL,
    `idpessoa` int NOT NULL,
    `depoimento` text NOT NULL,
    `datahora` datetime NULL DEFAULT CURRENT_TIMESTAMP,
    KEY `fk_emp_ped` (`idedicao`),
    KEY `fk_cli_ped` (`idpessoa`),
    CONSTRAINT `fk_depoimento_idedicao` FOREIGN KEY(`idedicao`) REFERENCES `edicoes`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE
    CONSTRAINT `fk_depoimento_pessoa` FOREIGN KEY(`idpessoa`) REFERENCES `pessoas`(`id`) on delete restrict on update cascade;

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- adicionando foreign key
ALTER TABLE depoimentos ADD
CONSTRAINT `fk_depoimento_teste` FOREIGN KEY(`idpessoa`) 
REFERENCES `pessoas`(`id`) on delete restrict on update cascade;

-- remover foreign key
ALTER TABLE depoimentos drop constraint fk_depoimento_pessoa;