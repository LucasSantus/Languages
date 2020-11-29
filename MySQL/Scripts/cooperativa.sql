
-- Dropando o database "cooperativa", caso existir
DROP DATABASE IF EXISTS cooperativa;

-- Criando database "cooperativa", caso não existir
CREATE DATABASE IF NOT EXISTS cooperativa;

-- Utilizando banco de dados "cooperativa"
use cooperativa;

SET FOREIGN_KEY_CHECKS = 0;

-- Dropando a tabela "habilidades", caso existir
DROP TABLE IF EXISTS `habilidades`;

-- Criando a tabela "habilidades", caso não existir
CREATE TABLE IF NOT EXISTS `habilidades`(
  `id` int UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `habilidade` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com os dados das habilidades';

--
-- Dumping data for table `habilidades`
--

LOCK TABLES `habilidades` WRITE;
INSERT INTO `habilidades` VALUES (1,'Artesã(o)'), (2,'Tapeceiro(a)'), (3,'Costureiro(a)'), (4,'Pintor(a)'), (5,'Ouvires');
UNLOCK TABLES;



-- Dropando a tabela "tipos_produtos", caso existir
DROP TABLE IF EXISTS `tipos_produtos`;

-- Criando a tabela "tipos_produtos", caso não existir
CREATE TABLE IF NOT EXISTS `tipos_produtos`(
  `id` int UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `tipo_produto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com os tipos dos produtos';

--
-- Dumping data for table `tipos_produtos`
--

LOCK TABLES `tipos_produtos` WRITE;
INSERT INTO `tipos_produtos` VALUES (1,'Estátuas'), (2,'Bordados, Mantas e Estátuas'), (3,'Mantas'), (4,'Quadros'), (5,'Terços');
UNLOCK TABLES;



-- Criando a tabela "associar", caso não existir
CREATE TABLE IF NOT EXISTS `associar`(
  `id` int UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `idtipo_produto` int UNSIGNED NOT NULL,
  `idhabilidade` int UNSIGNED NOT NULL,
  KEY `fk_tprodutos_ass` (`idtipo_produto`),
  KEY `fk_habilidade_ass` (`idhabilidade`),
  CONSTRAINT `fk_tprodutos_ass` FOREIGN KEY (`idtipo_produto`) REFERENCES `tipos_produtos` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_habilidade_ass` FOREIGN KEY (`idhabilidade`) REFERENCES `habilidades` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela para associar os produtos';

--
-- Dumping data for table `associar`
--

LOCK TABLES `associar` WRITE;
INSERT INTO `associar` VALUES (1,1,1), (2,1,1), (3,2,2), (4,3,3), (5,4,4), (6,5,5);
UNLOCK TABLES;



-- Dropando a tabela "pessoas", caso existir
DROP TABLE IF EXISTS `pessoas`;

-- Criando tabela "pessoas", caso não existir
CREATE TABLE IF NOT EXISTS `pessoas`(
  `id` int UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `id_associar` int UNSIGNED NOT NULL,
  KEY `fk_habilidade_pes` (`id_associar`),
  CONSTRAINT `fk_habilidade_pes` FOREIGN KEY (`id_associar`) REFERENCES `associar` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com os dados das pessoas & suas habilidades';

--
-- Dumping data for table `pessoas`
--

LOCK TABLES `pessoas` WRITE;
INSERT INTO `pessoas` VALUES (1,'Joaquim Honório',1), (2,'Josefina Marcolino',1), (3,'Carlos Camilo Resende',2), (4,'Serafim Cascardo',3), (5,'Maria de Lourdes Ferrari',4), (6,'Maria Clara Carmolina',4), (7,'Ana Lúcia Faria',4), (8,'Carmelia Catarina Souza',5), (9,'Sueli Santos e Silva',5);
UNLOCK TABLES;



-- Dropando a tabela "clientes", caso existir
DROP TABLE IF EXISTS `clientes`;

-- Criando tabela "clientes", caso não existir
CREATE TABLE IF NOT EXISTS `clientes`(
  `id` int unsigned primary key NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL COMMENT 'email obrigatório!',
  `telefone` varchar(100) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com os dados dos clientes';

--
-- Dumping data for table `pessoas`
--

LOCK TABLES `clientes` WRITE;
INSERT INTO `clientes` VALUES (1,'Tadeu Amarantes','tadeu@hotmail.com','35 3222-4452'), 
(2,'Marcela Junqueira','Mjmm2020@hotmail.com','35 99958-5888'), 
(3,'SalviaSorisos','salvinha@sorrisos.com.br', ''), 
(4,'Solange Salimeni','solsal@gmail.com','31 2522-5887'), 
(5,'Evaristo das Dores','evaldor@doristo.com','27 99785-4458'), 
(6,'Manuel Henrique Salvo','mansalvo@dogma.com','21 3598-5578'), 
(7,'Jorge Tavares Torres','Jtt1980@gmail.com','31 35899-5458');
UNLOCK TABLES;



-- Dropando a tabela "pedidos", caso existir
DROP TABLE IF EXISTS `pedidos`;

-- Criando tabela "pedidos", caso não existir
CREATE TABLE IF NOT EXISTS `pedidos`(
  `id` int unsigned primary key NOT NULL AUTO_INCREMENT,
  `id_cliente` int unsigned NOT NULL,
  `id_tipo-produto` int unsigned NOT NULL,
  `descricao` varchar(200) NULL,
  `data_pedido` date NOT NULL,
  `status` ENUM('1','2','3','0') NOT NULL COMMENT "1 - AGUARDANDO, 2 - FABRICANDO, 3 - ENTREGUE, 0 - CANCELADO"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabela com as informações dos pedidos';

--
-- Dumping data for table `pessoas`
--

LOCK TABLES `pedidos` WRITE;
INSERT INTO `pedidos` VALUES (1, 1, 4, 'São Jorge', '2020-01-01', 1), (2, 1, 1,'São Francisco', '2020-02-01', 2), (3, 3, 5,'Rosário', '2020-03-25', 3), (4, 4, 5,'Rosário de Vidro', '2020-03-30', 3), (5, 6, 2,'Capa de Nsa. Sra. Aparecida', '2020-05-18', 1), (6, 7, 4,'Sagrada Família', '2020-05-14', 2), (7, 7, 1,'Santa Helena', '2020-09-10', 2), (8, 7, 5,'Rosário de Vidro', '2020-07-07', 1), (9, 7, 4,'São Francisco', '2020-06-08', 2), (10, 3, 4,'São Sebastião', '2020-08-12', 3),(11, 3, 1,'São Bento', '2020-10-19', 1);
UNLOCK TABLES;

SET FOREIGN_KEY_CHECKS = 1;
